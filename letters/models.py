from django.db import models
from accounts.models import User
from django.utils import timezone

class Contact(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    name= models.CharField(null=True, blank=True)
    email= models.EmailField(null=False, blank=False)
    created_date= models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ['user', 'email']

class Letter(models.Model):

    STATUS_NOT_SCHEDULED = 'not_scheduled'
    STATUS_SCHEDULED = 'scheduled'
    STATUS_SENT = 'sent'
    STATUS_FAILED= 'failed'

    STATUS_CHOICES = [
        (STATUS_NOT_SCHEDULED, 'Not Scheduled'),
        (STATUS_SCHEDULED, 'Scheduled'),
        (STATUS_SENT, 'Sent'),
        (STATUS_FAILED, 'Failed')
    ]
    
    author= models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    receiver= models.EmailField(null=False)
    subject= models.CharField(max_length=255, null=False)
    message= models.TextField(null=False)
    created_date= models.DateTimeField(auto_now_add=True, null=False)
    scheduled_date= models.DateTimeField(blank=True, null=True)
    sent_date= models.DateTimeField(blank=True, null=True)
    status= models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_NOT_SCHEDULED,
        null=False)

    def __str__(self):
        return self.subject