#ACCOUNT MODELS
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import secrets

class UserToken(models.Model):
    TOKEN_TYPES=[
        ('verify_email','Verify Email'),
        ('change_email','Change Email'),
        ('reset_password','Reset Password')
    ]

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    token=models.CharField(max_length=100, null=False, unique=True)
    token_type=models.CharField(max_length=20, null=False, choices=TOKEN_TYPES)
    created_at=models.DateTimeField(auto_now_add=True, null=False)
    expires_at=models.DateTimeField(null=False)
    is_used=models.BooleanField(default=False, null=False)
    pending_email = models.EmailField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = secrets.token_urlsafe(48)
        if not self.expires_at:
            if self.token_type == 'reset_password':
                self.expires_at = timezone.now() + timezone.timedelta(hours=1)
            else:
                self.expires_at = timezone.now() + timezone.timedelta(hours=24)
        super().save(*args, **kwargs)
    
    def is_valid(self):
        return not self.is_used and timezone.now() < self.expires_at
    
    def __str__(self):
        return f"{self.user.username} - {self.token_type} - {self.is_valid()}"
