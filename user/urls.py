from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('register/', views.register, name='register'),
    path('designers/', views.designers, name='designers'),
    path('profile/<str:pk>/', views.profile, name="profile"),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('edit_profile/<str:pk>/', views.edit_profile, name='edit_profile'),
]
