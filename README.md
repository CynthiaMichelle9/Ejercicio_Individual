# Ejercicio Individual 6
# Creación de grupos y usuarios desde el administrador de Django 

## Se crean dos grupos de usuarios con sus respectivos dos usuarios: 

1. Grupo `Soporte técnico` encargado de la atención remota de los usuarios registrados en la aplicación.

usuario: soporte1
usuario: soporte2


2. Grupo `Recursos humanos`  encargado de la contratación y/o despidos de los grupos y usuarios.

usuario:  RH1
usuario: RH2


## Permisos diferenciados

Al asignar permisos diferenciados, estamos asegurando que cada grupo de usuarios tenga acceso solo a las funcionalidades y acciones necesarias para cumplir sus roles y responsabilidades específicas. 

### Soporte técnico

El grupo `Soporte` posee los permisos tanto para revisar la información de los usuarios como la de realizar modicaciones o cambios a dicha información, en caso de ser contactados por los usuarios. 

## Permisos de Recursos humanos

El grupo `Recursos humanos` posee los permisos para ver y editar, tanto grupos como usuarios de la aplicación. Además puede agregar o eliminar personal del sistema. 
Personal encargado de la contratación y/o despidos de los grupos y usuarios. Posee todos los permisos de los usuarios y grupos del sistema.