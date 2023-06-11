from django.urls import path
from .views import IndexView, tabla_usuarios, RegistroView

urlpatterns = [
    path('', IndexView.as_view(template_name='index.html'), name='Home'),
    path('usuarios/', tabla_usuarios,  name='Usuarios'),
    path('registro/', RegistroView.as_view(), name='Registro')
]
