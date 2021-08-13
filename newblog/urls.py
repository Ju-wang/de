from django.urls import path, include
from . import views

urlpatterns = [
    path('main/', views.main, name="main"),
    path('main/visiter/', views.visiter, name="visiter"),
    path('main/visiter/<int:id>/', views.detail, name="detail"),
    path('main/visiter/new/', views.new, name="new"),
    path('main/visiter/<int:id>/add_comment/', views.add_comment, name="add_comment"),
]