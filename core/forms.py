from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    admin = forms.BooleanField(help_text='For shop/outlet account')

    class Meta:
        model = User
        fields = ('username', 'admin', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)
            self.fields['admin'].required = False