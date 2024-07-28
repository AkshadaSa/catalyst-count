from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index_view, name='index'),  # Add this line to handle the root URL
    path('login/', views.login_view, name='login'),
    path('upload/', views.upload_view, name='upload'),
    path('query-builder/', views.query_builder_view, name='query_builder'),
    path('users/', views.users_view, name='users'),
]
