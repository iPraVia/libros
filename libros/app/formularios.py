from django import forms

class IniciarSesion(forms.Form):
    email = forms.CharField(label='Correo Electronico',label_suffix='')
    password = forms.CharField(widget=forms.PasswordInput(),label_suffix='')

    email.widget.attrs['class'] = 'form-control'
    password.widget.attrs['class'] = 'form-control'

class userRegistrationForm(forms.Form):
    nombre = forms.CharField(label_suffix='')
    apellido = forms.CharField(label='Primer Apellido',label_suffix='')
    rut = forms.CharField(label_suffix='')
    celular = forms.CharField(label_suffix='')
    email = forms.CharField(label='Correo electronico',label_suffix='')
    password = forms.CharField(widget=forms.PasswordInput(),label_suffix='')
    terminos = forms.BooleanField(label='',required = True, disabled = False, widget=forms.widgets.CheckboxInput(attrs={'class':'checkbox-inline','value':False,'name':'terminos'}), help_text = "Acepto los terminos y condiciones", error_messages ={'required':'Debe aceptar los terminos y condiciones si desea registrarse'} )
    
    nombre.widget.attrs['class'] = 'form-control'
    apellido.widget.attrs['class'] = 'form-control'
    rut.widget.attrs['class'] = 'form-control'
    celular.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    password.widget.attrs['class'] = 'form-control'