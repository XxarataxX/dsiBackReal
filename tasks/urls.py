from django.urls import path, re_path
from . import views

app_name = 'tasks'

urlpatterns = [

    path('lista_tarea/', views.ConditionListApiView.as_view(), name='lista_tarea'),

    path(
        'lista_tarea_detail/<pk>',
        views.DetailTarea.as_view()
        ), 
]