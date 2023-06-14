from django.urls import path
from .views import IndexView, tabla_usuarios, RegistroView, RegistroView, SesionView, MicuentaView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', IndexView.as_view(template_name='index.html'), name='Home'),
    path('usuarios/', tabla_usuarios,  name='Usuarios'),
    path('registro/', RegistroView.as_view(), name='Registro'),
    path('login/', SesionView.as_view(), name='Login'),
    path('logout/', LogoutView.as_view(), name='Logout'),
    path('micuenta/', MicuentaView.as_view(), name='Micuenta'),
]
