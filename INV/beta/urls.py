from django.urls import path
from beta import views
urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('gallery', views.gallery, name='gallery'),
    path('event', views.event, name='event'),
    path('upcoming', views.upcoming, name='upcoming'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('form', views.form, name='form'),
]