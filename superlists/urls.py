from django.urls import path
from lists import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('lists/odin-edinstvennii-spisok-v-mire/', views.view_list, name='view_list'),
]
