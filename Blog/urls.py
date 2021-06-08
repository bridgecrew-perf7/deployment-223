from django.urls import path
from. import views

app_name = 'Blog'
urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('<int:blog_id>/', views.detail, name='detail'),
]