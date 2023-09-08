from django.urls import path, re_path
from . import views

app_name = 'tasks'

urlpatterns = [

    path('lista_tarea/', views.ConditionListApiView.as_view(), name='lista_tarea'),

    path(
        'lista_tarea_detail/<int:id>',views.DetailTarea.as_view()
        ), 
    path(
        'tareas_tecnico/<int:tecnico_id>',views.ListTareaTecnico.as_view()
        ), 
]