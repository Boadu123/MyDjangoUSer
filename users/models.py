import uuid
from django.db import models
from django.contrib.auth.models import User

class UserModel(User):
    ROLE_CHOICES = [
        ('Customer', 'Customer'),
        ('Cleaner', 'Cleaner/Provider')
    ]

    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    profile_image_url = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    last_login_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    ai_order_preferences = models.JSONField(blank=True, null=True)

    

    def __str__(self):
        return self.username