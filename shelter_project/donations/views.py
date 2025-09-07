"""Views for all the actions takes place. Interaction with database: save, retrive and update"""
from django.shortcuts import render, redirect
from django.db.models import Sum
from django.urls import reverse
from .models import Donation, Distribution, Donor, DonationType
from .forms import DonationForm, DistributionForm
from django.contrib import messages

def home(request):
    """Return the inventory list"""
    return redirect('inventory_list')

def add_donation(request):
    """Add new donation record."""
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Donation recorded.')
            return redirect(reverse('inventory_list'))
    else:
        form = DonationForm()
    return render(request, 'donations/add_donation.html', {'form': form})

def distribute(request):
    """Post request is to submit distribution update to databse."""
    if request.method == 'POST':
        form = DistributionForm(request.POST)
        if form.is_valid():
            dist = form.save(commit=False)
            donated = Donation.objects.filter(donation_type=dist.donation_type).aggregate(total=Sum('amount'))['total'] or 0
            distributed = Distribution.objects.filter(donation_type=dist.donation_type).aggregate(total=Sum('amount'))['total'] or 0
            available = donated - distributed
            if dist.amount <= available:
                dist.save()
                messages.success(request, 'Distribution recorded.')
                return redirect(reverse('inventory_list'))
            else:
                messages.error(request, f'Insufficient inventory: available {available}, tried to distribute {dist.amount}.')
    else:
        form = DistributionForm()
    return render(request, 'donations/distribute.html', {'form': form})

def inventory_report(request):
    """Inventory list retrival."""
    donations = Donation.objects.values('donation_type__name').annotate(total_donated=Sum('amount'))
    distributions = Distribution.objects.values('donation_type__name').annotate(total_distributed=Sum('amount'))
    report = {}
    for d in donations:
        report[d['donation_type__name']] = {'donated': float(d['total_donated']), 'distributed': 0.0}
    for dis in distributions:
        name = dis['donation_type__name']
        if name in report:
            report[name]['distributed'] = float(dis['total_distributed'])
        else:
            report[name] = {'donated': 0.0, 'distributed': float(dis['total_distributed'])}
    for k, v in report.items():
        v['available'] = v['donated'] - v['distributed']
    # sort by type name
    report = dict(sorted(report.items()))
    return render(request, 'donations/inventory_report.html', {'report': report})

def donor_report(request):
    """Donor's list."""
    donors = Donor.objects.annotate(total=Sum('donation__amount')).order_by('-total')
    return render(request, 'donations/donor_report.html', {'donors': donors})
