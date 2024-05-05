from django import forms
from .models import Profile, User


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))


class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control my-2'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control my-2',
        'placeholder': 'Password confirm'}))

    class Meta:
        fields = (
            'username',
            'email',
            'first_name',
            'last_name'
        )
        model = User

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control my-2',
                'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control my-2',
                'placeholder': 'example@gmail.com'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control my-2',
                'placeholder': 'First name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control my-2',
                'placeholder': 'Last name'
            })
        }

    def clean_password2(self):
        password2 = self.cleaned_data.get("password2")
        if password2 != self.cleaned_data["password"]:
            raise forms.ValidationError("Password not match!")

        return password2

    def clean_email(self):

        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Bunday e-mailli faydalanuvchi mavjud!")

        return email


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'image',
            'birth_date',
        )
        widgets = {
            'image': forms.FileInput(attrs={
                'class': 'form-control my-2',
                'placeholder': 'Photo for profile'
            }),
            'birth_date': forms.DateInput(attrs={
                'class': 'form-control my-2', 'placeholder': "2000-01-01",
                'type': 'date'
            }),
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control my-2',
                'placeholder': 'example@gmail.com'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control my-2',
                'placeholder': 'First name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control my-2',
                'placeholder': 'Last name'
            })
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise forms.ValidationError("Bunday e-mailli faydalanuvchi mavjud!")

        return email
