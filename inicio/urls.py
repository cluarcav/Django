from django.urls import path
from .views import home, crear_autor, crear_categoria, crear_post, buscar_post

urlpatterns = [
    path("", home, name="home"),
    path("autor/nuevo/", crear_autor, name="crear_autor"),
    path("categoria/nueva/", crear_categoria, name="crear_categoria"),
    path("post/nuevo/", crear_post, name="crear_post"),
    path("post/buscar/", buscar_post, name="buscar_post"),
]