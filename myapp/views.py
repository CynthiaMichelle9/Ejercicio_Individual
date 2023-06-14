from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Usuario
from myapp.forms import FormularioRegistro, LoginForm


# Create your views here.
class IndexView(TemplateView):
    template_name='index.html'

    def get(self, request, *args, **kwargs):
       result = []
       if not result:
           print('error')
       context = {}
       return render(request, self.template_name, context=context)


def tabla_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'users.html', {'usuarios': usuarios})

class RegistroView(TemplateView):
    template_name = 'registro.html'

    def get(self, request, *arg, **kwargs):
        #context = super(RegistroView, self).get_context_data(**kwargs)
        #context["formulario"] = FormularioRegistro()
        formulario = FormularioRegistro()
        return render(request, self.template_name, {"formulario": formulario})
    
    def post(self, request, *arg, **kwargs):
        form= FormularioRegistro(request.POST)
        mensaje = {
            "enviado": False,
            "resultado": None
        }

        if form.is_valid():
            username =form.cleaned_data['nombre de usuario']
            nombre =form.cleaned_data['nombre']
            apellido =form.cleaned_data['apellido']
            email =form.cleaned_data['email']
            telefono =form.cleaned_data['telefono']

            registrarusuario = Usuario(

                username=username,
                nombre=nombre,
                apellido=apellido,
                email=email, 
                telefono=telefono,
            )
            registrarusuario.save()

            mensaje = {"enviado": True, "resultado": "Gracias por registrarte "}
        else:
            mensaje =  {"enviado": True, "resultado": form.errors}

        return render(request, self.template_name, {"formulario": form, "mensaje": mensaje })

class SesionView(TemplateView):
    template_name = 'registration/login.html'

    def get(self, request, *arg, **kwargs):
        form = LoginForm
        return render(request, self.template_name,{"formulario": form})
    
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('Home')
        form.add_error(None, 'Credenciales incorrectas')  # Agrega un error general al formulario
        return render(request, self.template_name, {"formulario": form})