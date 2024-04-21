from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("", views.inicio , name="home"),

    #path("alta_curso/<nombre>", views.alta_curso),
    path("add_profesor", views.profesor_formulario , name="profesor"),
    path("add_alumno", views.alumnos_formulario , name="alumnos"),
    path("alta_curso", views.curso_formulario , name='add_cursos'),

    path("buscar_profesores", views.buscar_profesores, name='buscar_profesores'),
    path("buscar_alumnos", views.buscar_alumnos, name='buscar_alumnos'),
    path("buscar_curso", views.buscar_curso, name='buscar_cursos'),

    path("list_alumnos", views.ver_alumnos, name="ver_alumnos"),
    path("list_profesores", views.ver_profesores , name="ver_profesores"),
    path("ver_cursos",  views.ver_cursos , name="cursos"),

    path("resultado_alumnos", views.resultado_alumnos, name='resultado_alumnos'),
    path("resultado_profesores", views.resultado_profesores, name='resultado_profesores'),
    path("buscar", views.buscar),

    path("eliminar_curso/<int:id>", views.elimina_curso, name="elimina_curso"),
    path("eliminar_alumno/<int:id>", views.elimina_alumno, name="elimina_alumno"),
    path("eliminar_profesor/<int:id>", views.elimina_profesor, name="elimina_profesor"),




    path("editar_curso/<int:id>" , views.editar , name="editar_curso"),
    path("editar_alumno/<int:id>" , views.editar_alumno , name="editar_alumno"),
    path("editar_profesor/<int:id>" , views.editar_profesor , name="editar_profesor"),
    
    path("register", views.register, name="Register"),

    path("login", views.login_request , name="Login"),
    path("logout" , LogoutView.as_view(template_name="logout.html") , name="Logout"),
    
    path("editarPerfil" , views.editarPerfil , name="EditarPerfil")

    

]
