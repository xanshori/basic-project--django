from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.utils import ErrorList

class UserLogin(forms.Form):
    username = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Username',
            }
        )
    )
    password = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'******'
            }
        )
    )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name',
            'email',
            'username',
            'career',
            'bio',
            'profile_image',
            'profile_header',
        ]
        widgets={
            'name': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'career': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'bio': forms.Textarea(
                attrs={
                    'class':'form-control',
                    "cols":'3',
                }
            ),
            'profile_image': forms.FileInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'profile_header': forms.FileInput(
                attrs={
                    'class':'form-control'
                }
            ),
        }

class UserRegister(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Password'
            }
        ),
        help_text=  '''
        <ol> 
            <li>Your password can't be too similar to your other personal information.</li>
            <li>Your password must contain at least 8 characters.</li>
            <li>Your password can't be a commonly used password.</li>
            <li>Your password can't be entirely numeric.</li>
        </ol>                
        '''
        
        )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Password confirmation'
            }
        ),
        strip=False,
        help_text='''Enter the same password as before, for verification.''',
    )
    
    first_name= forms.CharField(
        required=True,
        label='name',
        widget=forms.TextInput(
    
            attrs={
                'class':'form-control',
                'placeholder':'name'
            }
        ),
        strip=False,
        help_text='name required',
    )
    phone = forms.CharField(
        required=True,
        max_length= 16,
        label='Phone Number',
        widget=forms.TextInput(
    
            attrs={
                'class':'form-control',
                'placeholder':'phone'
            }
        ),
        strip=False,
        help_text='required phone number ',
    )
    class Meta:
        model = User
        fields=(
            'username',
            'email',
            'first_name',
            'phone',
            'password1',
            'password2',
        )
        widgets={
            'username':forms.TextInput(
                attrs={
                    'placeholder':'Username',
                    'class':'form-control',
                }
            ),
            'email':forms.TextInput(
                attrs={
                    'placeholder':'your@email.com',
                    'class':'form-control',
                }
            ),
        }


class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<div class="error alert alert-danger">%s</div>' % e for e in self])
