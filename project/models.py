from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy  as _


from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(_('email address'),unique=True)
    mobile_no = models.CharField(max_length=10,unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Account(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    account_balance = models.FloatField()

    def __str__(self):
        return self.user.email

class Recharge_Transaction(models.Model):
    payment_status_choices = (
        (1, 'SUCCESS'),
        (2, 'FAILURE' ),
        (3, 'PENDING'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    total_amount = models.FloatField()
    payment_status = models.IntegerField(choices = payment_status_choices, default=3)
    recharge_transaction_id = models.CharField(unique=True, max_length=100, null=True, blank=True, default=None) 
    datetime_of_payment = models.DateTimeField(default=timezone.now)
    # related to razorpay
    razorpay_order_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_payment_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_signature = models.CharField(max_length=500, null=True, blank=True)
    

    def save(self, *args, **kwargs):
        if self.order_id is None and self.datetime_of_payment and self.id:
            self.order_id = self.datetime_of_payment.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.user.email + " " + str(self.id)

class Channel_Integration(models.Model):
    company_name = models.CharField(max_length = 256)
    owner_name = models.CharField(max_length = 256)
    company_registered_address = models.CharField(max_length = 256)
    company_registered_email = models.EmailField(max_length = 256)
    company_register_mobile = models.BigIntegerField()
    company_id_proof = models.FileField(max_length = 256,upload_to="Channel_Integration_company_id_proof")
    individual_id_proof =models.FileField(max_length = 256,upload_to="Channel_Integration_individual_id_proof")
    company_GST = models.FileField(max_length = 256,upload_to="Channel_Integration_company_GST")

class Carrier_Integration(models.Model):
    company_name = models.CharField(max_length = 256)
    owner_name = models.CharField(max_length = 256)
    company_registered_email = models.EmailField(max_length = 256)
    company_register_mobile = models.BigIntegerField()
    company_GST = models.FileField(max_length = 256,upload_to="Carrier_Integration_company_GST")

class Order(models.Model):
    Pickup_Name = models.CharField(max_length = 256)
    Pickup_Mobile_Number = models.CharField(max_length = 10)
    Pickup_Alternate_Mobile_Number = models.CharField(max_length = 10)
    Pickup_Address1 = models.CharField(max_length=256)
    Pickup_Address2 = models.CharField(max_length=256)
    Pickup_Landmark = models.CharField(max_length=256)
    Pickup_City = models.CharField(max_length=256)
    Pickup_Pin_code = models.CharField(max_length=6)
    Delivery_Name = models.CharField(max_length = 256)
    Delivery_Mobile = models.CharField(max_length = 10)
    Delivery_Alternate_Mobile = models.CharField(max_length = 10)
    Delivery_Address1 = models.CharField(max_length=256)
    Delivery_Address2 = models.CharField(max_length=256)
    Delivery_Landmark = models.CharField(max_length=256)
    Delivery_City = models.CharField(max_length=256)
    Delivery_Pin_code = models.CharField(max_length=6)
