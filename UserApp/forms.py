from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import FeedBack


#User signup form using django's built in User model database
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']


#Feedback form using FeedBack model
class FeedbackForm(forms.ModelForm):
	class Meta:
		model = FeedBack
		fields = ['email','message']
			
