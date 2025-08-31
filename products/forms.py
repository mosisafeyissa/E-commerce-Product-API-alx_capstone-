# products/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Product # Import the Product model

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class UserLoginForm(AuthenticationForm):
    pass
    
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock_quantity', 'category', 'image_url']

class ProfileUpdateForm(UserChangeForm):
    password = None  # Prevents the password field from being rendered

    class Meta:
        model = User
        fields = ['username', 'email']