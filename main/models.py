from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from datetime import timedelta, datetime

class User(AbstractUser):
    trial_start_date = models.DateTimeField(auto_now_add=True)
    trial_active = models.BooleanField(default=True)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Custom reverse accessor to avoid conflicts
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Custom reverse accessor to avoid conflicts
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def trial_end_date(self):
        return self.trial_start_date + timedelta(days=14)

    def is_trial_expired(self):
        return datetime.now() > self.trial_end_date()
