from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name = 'inicio'),
    url('crear_persona', views.CreatePersona.as_view(), name = "crear_persona"),
    url(r'^listar_persona/',views.ListPersona.as_view(), name="listar_persona"),
    url(r'^editar_persona/(?P<id>\d+)/$',views.UpdatePersona.as_view(), name="editar_persona"),
    url(r'^eliminar_persona/(?P<id>\d+)/$',views.DeletePersona.as_view() , name="eliminar_persona"),
    ]