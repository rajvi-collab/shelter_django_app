"""Relational Tabular database creation. Use default databse Sqlite3."""
from django.db import models

class Donor(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class DonationType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    donation_type = models.ForeignKey(DonationType, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.donor} - {self.amount} {self.donation_type} on {self.date}"

class Distribution(models.Model):
    donation_type = models.ForeignKey(DonationType, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.amount} {self.donation_type} distributed on {self.date}"
