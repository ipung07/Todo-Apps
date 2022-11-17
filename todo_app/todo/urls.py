from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name="index"),
    path('detail/<int:id>/', views.detail, name="detail"),
    path('insert/', views.insert, name="insert"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('delete/<int:id>/', views.delete, name="delete"),
]
