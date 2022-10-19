from dataclasses import fields
#from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from DataMundial.models import Avatar
#from .models import BlogConcurso
from .models import MyModelBlog

class form_registros(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    edad = forms.IntegerField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']
        help_text = {k:"" for k in fields}

class UserEditForm(UserChangeForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(widget = forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        help_text = {k:"" for k in fields}

class ChangePasswordForm(PasswordChangeForm):
    old_password= forms.CharField(label="", widget= forms.PasswordInput(attrs={'placeholder': "Old Passqord", }))
    new_password1= forms.CharField(label="", widget= forms.PasswordInput(attrs={'placeholder': "New Password", }))
    new_password2= forms.CharField(label="", widget= forms.PasswordInput(attrs={'placeholder': "Confirm new Password", }))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'newpassword2']
        help_text = {k:"" for k in fields}


class AvatarFormulario(forms.Form):
    avatar = forms.ImageField()


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()


# class ConcursoBlog(forms.Form):
#     comentario_blog = forms.CharField()
#     autor = forms.CharField()
#     # concurso = forms.CharField(widget=forms.Textarea)
#     class Meta:
#         model = User
#         fields = ['comentario_blog', 'autor']
#         help_text = {k:"" for k in fields}

# class BlogForm(forms.ModelForm):
#     class Meta:
#         model = BlogConcurso
#         fields = ["comentario", "autor",]
#         labels = {'comentario': "Comentario", "autor": "Autor",}

class MyForm(forms.ModelForm):
    class Meta:
        model = MyModelBlog
        fields = ["comentario", "pais", "user", "fecha"]
        labels = {'comentario': "Escribe tu comentario:", "pais": "Pais Ganador", "user": "username", "fecha":"fecha"}

# class MyForm(forms.ModelForm):
#     class Meta:
#         model = MyModelBlog
#         fields = ["comentario", "pais"]
#         labels = {'comentario': "Escribe tu comentario:", "pais": "Pais Ganador"}

class form_mensaje(forms.Form):
    useror = forms.CharField(max_length=30)
    userdest = forms.CharField(max_length=30)
    mensaje = forms.CharField(max_length=300)