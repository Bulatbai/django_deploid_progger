

from dataclasses import fields
from django import forms
      
from .models import Post, Comments, Image
from django.contrib.auth.forms import UserCreationForm
from random import randrange as rand_num
from django.contrib.auth.models import User
class Postforms(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['user','name', 'location', 'description', 'amount_p','price']
        


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image','description', 'amount_p','price' )

class LetRegisterform(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
   
    class Meta:
      model = User
      fields = ('username', 'first_name', 'email')
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
        
            
 

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)




class Coment_Form(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['post','text']





 