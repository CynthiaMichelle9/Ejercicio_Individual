# Ejercicio Indiviudal 5.
## Funcionalidades de mi aplicación: Login/logout y restricciones incorporadas.

Este archivo README proporciona una explicación del desarrollo de la funcionalidad de login/logout en mi página web e incluye la explicación detallada de las restricciones de acceso creadas. 

1. Login / Logout
2. Restricciones de acceso

## Views.py

La clase `SesionView` es una subclase de `TemplateView` en Django, lo que significa que hereda la funcionalidad para renderizar una plantilla y mostrarla al usuario. 
Posee el atributo - `template_name`: Especifica el nombre de la plantilla que se utilizará para representar la página de inicio de sesión, en este caso corresponde a `registration/login.html`

## Plantilla 'login.html'

Se crea dentro de la carpeta templates/my app una carpeta `registration` para guardar `login.html` que contiene el formulario que despliega el Login para iniciar sesión.

Ccon el método `post` se envía y valida el usuario y su contraseña. Si el usuario es autenticado, redirige a la página 'Micuenta' que despliega información personalizada para el usuario con un mansaje de bienvenida. En caso contrario, marca un mensaje de error.

```
def post(self, request, *args, **kwargs):
      form = LoginForm(request.POST)
      if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
          if user.is_active:
            login(request, user)
            return redirect('Micuenta')
        form.add_error('username', 'El nombre de usuario o la contraseña son incorrectos. Por favor, inténtalo nuevamente.')
        return render(request, self.template_name, { "form": form })
      else:
        return render(request, self.template_name, { "form": form })

```

## Restricción de acceso

Se añade la restricción de acceso, en caso de ser un usuario no registrado en la página no se puede acceder `localhost:800/micuenta` y redirige nuevamente a la página del formulario de acceso `login.html`.
La vista está decorada, lo que indica que se requiere autenticación para acceder a esta vista. Si un usuario no está autenticado, se le redirigirá a la página de inicio de sesión. 

```
@method_decorator(login_required, name='dispatch')
class MicuentaView(TemplateView):
    template_name = 'micuenta.html'
    @login_required
    def bienvenida(request):
        username = request.user.username
        return render(request, 'micuenta.html', {'username': username})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.get_username()
        return context

```

### 

En la plantilla `base.html` se agrega una sección de código para cambiar la vista de la barra de navegación en caso de ser un usuario autenticado utilizando

```
 {% if user.is_authenticated %}

    BARRA DE NAVEGACIÓN PERSONALIZADA PARA USUARIOS AUTENTICADOS
    
 {% endif %}
```

## urls.py

Se agregan las rutas a la lista de URL de myapp.

```
    .
    .
    .
    path('login/', SesionView.as_view(), name='Login'),
    path('logout/', LogoutView.as_view(), name='Logout'),
    path('micuenta/', MicuentaView.as_view(), name='Micuenta'),

```

## forms.py

Se creó la classe de formulario `LoginForm`. Esta clase hereda de forms.Form, lo que indica que es un formulario básico de Django que se utiliza para capturar y validar los datos del formulario. 

### Parámetros

- El parámetro label establece el texto de etiqueta del campo. 
- El parámetro required=True indica que el campo es obligatorio. 
- Los parámetros max_length y min_length especifican las longitudes máxima y mínima permitidas para el campo, respectivamente. 
- El parámetro error_messages proporciona mensajes de error personalizados para diferentes validaciones. 

La clase define un formulario de inicio de sesión con dos campos: username y password. Estos campos tienen reglas de validación, mensajes de error personalizados y widgets que se utilizan para renderizar los campos en HTML.
 
 
### Credenciales

En caso de necesitar crear un usuario puede realizarlo desde el administrador de django utilizando las siguientes credenciales:
- nombre de usuario: admin
- contraseña: 123