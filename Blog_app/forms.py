# Override the UserCreationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.forms import TextInput, EmailInput, PasswordInput


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email', error_messages={'exists': 'This already exists!'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        # widgets = {
        #     'username': TextInput(attrs={
        #
        #         'id': 'username',
        #         'name': 'username',
        #         'placeholder': 'UserName',
        #         'required': 'required'
        #     }),
        #     'email': EmailInput(attrs={
        #         'id': 'email',
        #         'name': 'email',
        #         'placeholder': 'Email',
        #         'required': 'required'
        #     }),
        #     'password1': PasswordInput(attrs={
        #
        #         'id': 'password',
        #         'placeholder': 'jjj',
        #         'required': 'required'
        #     }),
        #     'password2': PasswordInput(attrs={
        #         'id': 'password',
        #         'placeholder': '********',
        #         'required': 'required'
        #     })
        # }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs['class'] = 'form-control'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            self.fields[field_name].widget.attrs.update({
                "placeholder": field.label,
                'class': "form-control"
            })

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(self.fields['email'].error_messages['exists'])
        return self.cleaned_data['email']

