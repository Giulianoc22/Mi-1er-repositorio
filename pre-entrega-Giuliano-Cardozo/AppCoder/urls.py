from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio , name="home"),
    path("ver_cursos", views.ver_cursos , name="cursos"),
    #path("alta_curso/<nombre>", views.alta_curso),
    path("add_alumno", views.alumnos_formulario , name="alumnos"),
    path("alta_curso", views.curso_formulario , name='add_cursos'),
    path("buscar_curso", views.buscar_curso, name='buscar_cursos'),
    path("buscar", views.buscar),
    path("add_profesor", views.profesor_formulario , name="profesor"),
    path("list_alumnos", views.ver_alumnos, name="ver_alumnos"),
    path("list_profesores", views.ver_profesores , name="ver_profesores"),
    path("buscar_alumnos", views.buscar_alumnos, name='buscar_alumnos'),
    path("resultado_alumnos", views.resultado_alumnos, name='resultado_alumnos'),
    path("buscar_profesores", views.buscar_profesores, name='buscar_profesores'),
    path("resultado_profesores", views.resultado_profesores, name='resultado_profesores')
    

]
