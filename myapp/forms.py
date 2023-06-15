from django import forms


class FormularioRegistro(forms.Form):
    username = forms.CharField(label='Nombre de usuario', required=True, max_length=15, 
                             error_messages={
                                 'required': 'El nombre de usuario es obligatorio',
                                 'max_length': 'El nombre de usaurio es muy largo, restringir a 15 caracteres',
                             },
                             widget=forms.TextInput(attrs={
                                'placeholder': 'Ingrese su nombre de usuario', 
                                'class':'form-control'
                             }))
    nombre = forms.CharField(label='Nombre', required=True, max_length=30, 
                             error_messages={
                                 'required': 'El nombre es obligatorio',
                                 'max_length': 'El nombre es muy largo',
                             },
                             widget=forms.TextInput(attrs={
                                'placeholder': 'Ingrese su nombre', 
                                'class':'form-control'
                             }))
    apellido = forms.CharField(label='Apellido', required=True, max_length=30,
                             error_messages={
                                 'required': 'El apellido es obligatorio',
                                 'max_length': 'El apellido es muy largo'
                             },
                             widget=forms.TextInput(attrs={
                                'placeholder': 'Ingrese su apellido', 
                                'class':'form-control'
                             }))
    email = forms.EmailField(label='Email', required=True, max_length=100,
                             error_messages={
                                 'required': 'El email es obligatorio',
                                 'max_length': 'El email es muy largo'
                             },
                             widget=forms.TextInput(attrs={
                                'placeholder': 'Ingrese su email', 
                                'class':'form-control'
                             }))
    telefono = forms.CharField(label='Teléfono', required=True, max_length=12,
                             error_messages={
                                 'required': 'El teléfono es obligatorio',
                                 'max_length': 'Ingrese 12 dígitos'
                             },
                             widget=forms.TextInput(attrs={
                                'placeholder': 'Ingrese su teléfono', 
                                'class':'form-control'
                             }))
    contraseña = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={
                            'placeholder': 'Ingrese su contraseña', 
                            'class':'form-control'
                            }), strip=False)
    
class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', required=True, max_length=20, min_length=5,
                           error_messages={
                               'required': 'El Usuario es obligatorio',
                               'max_length': 'El Usuario no puede superar los 20 caracteres',
                               'min_length': 'La contraseña debe tener al menos 5 caracteres'
                           },
                           widget=forms.TextInput(attrs={
                               'placeholder': 'Ingrese su nombre de usuario',
                               'class': 'form-control'
                           }))
    password = forms.CharField(label="Contraseña", required=True, max_length=20, min_length=5,
                               error_messages={
                                   'required': 'La contraseña es obligatoria',
                                   'max_length': 'La contraseña no puede superar los 20 caracteres',
                                   'min_length': 'La contraseña debe tener al menos 5 caracteres'
                               },
                                widget=forms.PasswordInput(attrs={
                                    'placeholder': 'Ingrese su contraseña', 
                                    'class':'form-control'
                                }), strip=False)
