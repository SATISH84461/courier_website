from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Channel_Integration, Carrier_Integration, Order
from django.contrib.auth.models import User

from .models import CustomUser

class Channel_Integration_Form(forms.ModelForm):
    class Meta:
        model = Channel_Integration
        fields = ['company_name','owner_name','company_registered_address','company_registered_email','company_register_mobile','company_id_proof','individual_id_proof','company_GST',]

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':'form-control mt-1','placeholder':self.fields[i].label})
            self.fields[i].required = True

class Carrier_Integration(forms.ModelForm):
    class Meta:
        model = Carrier_Integration
        fields = ['company_name','owner_name','company_registered_email','company_register_mobile','company_GST',]

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':'form-control mt-1','placeholder':self.fields[i].label})
            self.fields[i].required = True


class User_login_form(forms.Form):
    email = forms.CharField()
    password = forms.CharField()
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['password'].widget = forms.PasswordInput()
        self.fields['email'].widget.attrs.update({'class':'form-control mt-1','placeholder': 'Email'})
        self.fields['password'].widget.attrs.update({'class':'form-control mt-1','placeholder': 'Password'})
        self.fields['email'].required = True
        self.fields['password'].required = True

class User_signup_form(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email','mobile_no','password1','password2']
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':'form-control mt-1','placeholder':self.fields[i].label})
            self.fields[i].required = True

class OTP_Verification(forms.Form):

    email_otp = forms.CharField(max_length=4,min_length=4)
    mobile_otp = forms.CharField(max_length=4,min_length=4)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['email_otp'].widget.attrs.update({'class':'form-control mt-1','placeholder': 'Email OTP'})
        self.fields['mobile_otp'].widget.attrs.update({'class':'form-control mt-1','placeholder': 'Mobile OTP'})
        self.fields['email_otp'].required = True
        self.fields['mobile_otp'].required = True

class Pickup_form_1(forms.Form):
    choice = (
        ("1","Document(below 500g)"),
        ("2","Document(equal to or above 500g)"),
        ("3","Non Document")
    )
    doc_type = forms.ChoiceField(choices=choice)
    pickup_code = forms.CharField(max_length=6)
    delivery_code = forms.CharField(max_length=6)
    weight = forms.CharField(max_length=6)
    length = forms.CharField(max_length=6)
    breadth = forms.CharField(max_length=6)
    height = forms.CharField(max_length=6)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':'form-control mt-1','placeholder':i})
            self.fields[i].required = True
        self.fields['length'].widget.attrs.update({'class':'form-control mt-1 col-3'})
        self.fields['breadth'].widget.attrs.update({'class':'form-control mt-1 col-3'})

class Order_Form(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':'form-control mt-1','placeholder':self.fields[i].label})
            self.fields[i].required = True

class Track_Order(forms.Form):
    tracking_id = forms.CharField(max_length=256)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['tracking_id'].widget.attrs.update({'class':'form-control mt-1','placeholder':'Tracking Id'})