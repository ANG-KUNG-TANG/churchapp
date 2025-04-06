from django.urls import path
from . import views
from django.conf.urls.i18n import set_language


urlpatterns = [
    path('', views.index, name='index'),
    path('user_login/', views.user_login, name='user_login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),  # Keep this one
    path('services/', views.services, name='services'),
    path('home/', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('facebook/', views.facebook, name='facebook'),
    path('twitter/', views.twitter, name='twitter'),
    path('instagram/', views.instagram, name='instagram'),
    path('login/', views.user_login, name='user_login'),  # Add this line
    #path('set_language/', set_language, name='set_language'),
    path('donations/', views.donations, name='donations'),
    path('process_donation/', views.process_donation, name='process_donation'),
    path('policies/', views.policies, name='policies'),
    path('terms/', views.terms, name='terms'),
    #path('adindex/', views.adindex, name='adindex'),  # Ensure this points to the correct view
]