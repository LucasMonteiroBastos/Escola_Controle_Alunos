from django.urls import path
from controle import views

urlpatterns = [
    path('', views.home),
    path('escola/create/', views.ApiHome.as_view()),
    path('escola/lista/', views.ApiHomeJson.as_view()),
    path('escola/Json/', views.Json.as_view()),
]
