"""Forms created to show on the Front end to the user."""
from django import forms
from .models import Donation, Distribution, Donor, DonationType

class DonationForm(forms.ModelForm):
    donor_name = forms.CharField(max_length=200, label='Donor name')
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = Donation
        fields = ['donor_name', 'donation_type', 'amount', 'date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['donation_type'].queryset = DonationType.objects.all()
        self.fields['donor_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['donation_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned = super().clean()
        name = cleaned.get('donor_name')
        if name:
            donor, _ = Donor.objects.get_or_create(name=name.strip())
            cleaned['donor'] = donor
        return cleaned

    def save(self, commit=True):
        instance = super(forms.ModelForm, self).save(commit=False)
        instance.donor = self.cleaned_data['donor']
        instance.donation_type = self.cleaned_data['donation_type']
        instance.amount = self.cleaned_data['amount']
        instance.date = self.cleaned_data['date']
        if commit:
            instance.save()
        return instance


class DistributionForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = Distribution
        fields = ['donation_type', 'amount', 'date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['donation_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control'})
