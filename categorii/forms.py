

from django import forms
from .models import Post, Comments
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
class Postforms(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['name', 'location', 'description', 'img','price']





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
        
            
 


class Coment_Form(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['post','text']




# class Feedbaclform(forms.ModelForm):
#     class Meta:
#         model = Feedback
#         fields = ['place', 'text']