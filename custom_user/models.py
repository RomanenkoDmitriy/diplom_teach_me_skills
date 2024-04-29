from django.db import models

from django.contrib.auth.models import AbstractUser
# from phonenumber_field.formfields import PhoneNumberField


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
