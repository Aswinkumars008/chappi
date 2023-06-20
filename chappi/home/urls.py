from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('cooldrinks/',views.cooldrinks,name="cooldrinks"),
    path('hotdrinks/', views.hotdrinks,name="hotdrinks"),
    path('snacks/',views.snacks,name="snacks"),
]
