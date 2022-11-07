from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Director, Film


class CreateDirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if Director.objects.filter(name=name).count() > 0:
            raise ValidationError('This Director already exists')
        return name


class CreateFilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'producer': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if Film.objects.filter(title=title).count() > 0:
            raise ValidationError('This film already exists, darling')
        return title


class UserCreateForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise ValidationError('This username already exists!')
        return username

    def clean_password1(self):
        password = self.cleaned_data['password']
        password1 = self.cleaned_data['password1']
        if password != password1:
            raise ValidationError('Passwords do not match')
        return password


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
