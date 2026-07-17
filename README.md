# proyecto-módulo-3
Entrega de proyecto módulo 3

En este proyecto quise plasmar una de mis aficiones por la Fórmula 1, cosa que se me hizo fácil querer un poco más el python.

Cree un acceso como interfaz segura, mediante consola que restringe el acceso al panel principal usando credenciales de administrador (admin / 1234).
Al entrar permite la captura de datos como nombre completo, escudería y piloto favorito, para generar un control de aficionados como yo, también agregue un control en el que no se duplique los alias. 

El sistema está dividido en archivos independientes como lo pide el proyecto, en donde:

1.- seguridad.py : se encuentra el sistema de autenticación por contraseña y control de intentos para resguardar la aplicación.

2.- procesos.py: cree las estructuras de datos globales junto con las funciones del negocio, utilizando:
Para cumplir con los requerimientos técnicos y optimizar el rendimiento, se utilizaron:
  - Listas (list): almacenando la lista de aficionados registrados en orden de ingreso.
  - Diccionarios (dict): para estructurar la información de cada aficionado con pares clave-valor (alias, nombre, escuderia, piloto).
  - Conjuntos (set): lo usé específicamente para el almacenamiento de los alias únicos, permitiendo verificar duplicados antes de guardar los datos.
    
3.- main.py: Es donde se va a activar el programa, digamos que es el  motor y punto de entrada de la aplicación. 



