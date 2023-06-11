from django import forms


class FormularioRegistro(forms.Form):
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
