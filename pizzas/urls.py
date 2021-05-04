from django.urls import path
from .import views

app_name = 'pizzas'

urlpatterns=[
    path('', views.index, name='index'),
    path('zas', views.zas, name='zas'),
    path('za/<int:pizza_id>/', views.za, name="za")
]