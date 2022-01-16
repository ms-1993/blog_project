from django.urls import path

from Blog_app import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('forgot/', views.forgot, name='forgot'),
    path('', views.blog_list, name='blog_list'),
    path('single_blog/', views.single_blog, name='single_blog'),

]

# MohanSunka10@123
