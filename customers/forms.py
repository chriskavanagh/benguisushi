from django import forms
from django.contrib.auth.models import User



# Create your forms here.
class UserCreateForm(forms.ModelForm):
    '''form to create a new user.'''
    email = forms.EmailField(label='Email Is Required', required=True)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email']
        
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords Don't Match")
        return password2
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email Already Exists")
        return email
        
    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        password = self.cleaned_data['password1']
        user.set_password(password)
        if commit:
            user.save()
        return user