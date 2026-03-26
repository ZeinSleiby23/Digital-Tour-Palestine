from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tour/', views.tour, name='tour'),
    path('register/', views.register, name='register'),
    
    # API
    path('api/station/<int:order>/', views.get_station_api, name='get_station_api'),


    path('guestbook/', views.guestbook_view, name='guestbook'),
    path('save-feedback/', views.save_feedback, name='save_feedback'),
]