from django import forms

class IniciarSesion(forms.Form):
    email = forms.EmailField(label='Correo Electronico')
    password = forms.CharField(widget=forms.PasswordInput())

    email.widget.attrs['class'] = 'form-control'
    password.widget.attrs['class'] = 'form-control'

class userRegistrationForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField(label='Primer Apellido')
    rut = forms.CharField()
    celular = forms.CharField()
    email = forms.EmailField(label='Correo electronico')
    password = forms.CharField(widget=forms.PasswordInput())
    terminos = forms.BooleanField(label='',required = True, disabled = False, widget=forms.widgets.CheckboxInput(attrs={'class':'checkbox-inline','value':False,'name':'terminos'}), help_text = "Acepto los terminos y condiciones", error_messages ={'required':'Debe aceptar los terminos y condiciones si desea registrarse'} )
    
    nombre.widget.attrs['class'] = 'form-control'
    apellido.widget.attrs['class'] = 'form-control'
    rut.widget.attrs['class'] = 'form-control'
    celular.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    password.widget.attrs['class'] = 'form-control'