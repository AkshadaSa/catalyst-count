from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('upload_data/', views.upload_data_view, name='upload_data'),
    path('query-builder/', views.query_builder_view, name='query_builder'),
    path('users/', views.users_view, name='users'),
]
