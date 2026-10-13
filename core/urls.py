# path: función para definir una ruta individual
from django.urls import path
# views: el archivo que acabás de escribir, en la misma carpeta
from . import views

# urlpatterns: lista de rutas que esta app entiende
urlpatterns = [
    # '': la URL vacía (la raíz de esta app) · views.inicio: la función que la atiende
    # name='inicio': un alias interno para referirse a esta ruta sin escribir la URL a mano
    path('', views.inicio, name='inicio'),
    # nueva ruta 'servicios/' → función views.servicios → alias 'servicios'
    path('servicios/', views.servicios, name='servicios'),
]
# path: función para declarar una ruta URL y a qué vista apunta
from django.urls import path
# views: el módulo con todas las funciones-vista de esta app
from . import views

# urlpatterns: la lista de rutas que Django revisa, en orden, para cada URL
urlpatterns = [
    # '': la página de inicio de la Semana 3 ("Hola desde MySQL"); no la borres
    path('', views.inicio, name='inicio'),
    # /servicios/: la vista de listado que ya existía desde la Semana 3
    path('servicios/', views.servicios, name='servicios'),
    # /servicios/nuevo/: formulario en blanco para crear un registro
    path('servicios/nuevo/', views.crear_servicio, name='crear_servicio'),
    # /servicios/<int:pk>/editar/: <int:pk> captura el id de la URL y lo pasa como argumento a la vista
    path('servicios/<int:pk>/editar/', views.editar_servicio, name='editar_servicio'),
    # /servicios/<int:pk>/eliminar/: mismo patrón, para la pantalla de confirmación de borrado
    path('servicios/<int:pk>/eliminar/', views.eliminar_servicio, name='eliminar_servicio'),
# cierra la lista urlpatterns
]