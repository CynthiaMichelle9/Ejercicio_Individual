from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15, blank=False, null=True)
    nombre = models.CharField(max_length=25, blank=False, null=True)
    apellido = models.CharField(max_length=25, blank=False, null=True)
    email = models.EmailField(max_length=100, blank=False, null=True)
    telefono = models.CharField(max_length=12,blank=False, null=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    def __str__(self):
         return f"{self.id}, {self.username}"