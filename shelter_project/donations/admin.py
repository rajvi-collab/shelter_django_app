"""This is to create the admin page, from where admin can view, delete and updates the record."""
from django.contrib import admin
from .models import Donor, DonationType, Donation, Distribution

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(DonationType)
class DonationTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('donor', 'donation_type', 'amount', 'date')
    list_filter = ('donation_type', 'date')

@admin.register(Distribution)
class DistributionAdmin(admin.ModelAdmin):
    list_display = ('donation_type', 'amount', 'date')
    list_filter = ('donation_type', 'date')
