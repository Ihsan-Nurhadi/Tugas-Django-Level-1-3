from django.urls import path
from latihan import views

urlpatterns =[
    path('',views.index, name='index')
]