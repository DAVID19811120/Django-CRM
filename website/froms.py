from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class SignUpForm(UserCreationForm):
    email = froms.EmailField(labe="", widget=froms.TextInput(attrs={'class':'from-control','placeholder':'Email Address'}))
    first_name = forms.CharField(labe="", max_length=100, widget=froms.TextInput(attrs={'class':'from-control','placeholder':'First Name'}))
    last_name = forms.CharField(labe="",max_length=100, widget=froms.TextInput(attrs={'class':'from-control','placeholder':'Last name'}))



    class Meta:
        model = User
        fields =('username','first_name','last_name','email','password1','password.')


    def __init__(self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="from-tex text-muted"><small>Reguired. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</samll></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class= "form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li>'

        self.fields['password2'].widget.attrs['class'] = 'from-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Psss'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted">'