from django.db import models

class Job(models.Model):

    STATUS_CHOICES = [
        ('applied',   'Applied'),
        ('interview', 'Interview'),
        ('offer',     'Offer'),
        ('rejected',  'Rejected'),
    ]

    company    = models.CharField(max_length=200)
    role       = models.CharField(max_length=200)
    status     = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    location   = models.CharField(max_length=200, blank=True)
    notes      = models.TextField(blank=True)
    applied_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.role} at {self.company}"