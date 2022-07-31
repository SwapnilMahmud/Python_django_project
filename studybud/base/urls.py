from django.urls import URLPattern, path
from . import views

urlpatterns=[
    path('', views.home, name="home"),
    path('about/',views.about, name="about"),
    path('contact/',views.contact,name="contact"),
    path('room/<str:pk>/',views.room,name="room"),
    path('main/',views.main,name="main")
]