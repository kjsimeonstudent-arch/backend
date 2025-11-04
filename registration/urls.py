from django.urls import path
from . import views

urlpatterns = [
    path('api/registration', views.register_user, name='register_user'),
    path('api/users', views.register_user, name='users'),

    # New endpoint for user detail (GET, PUT, DELETE)
    path('api/users/<int:pk>/', views.user_detail, name='user_detail'),

]


