from django.urls import path
from myapp import views

urlpatterns=[
    path('',views.home,name='home' ),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('product/',views.product,name='product'),
    path('services/',views.services,name='services'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('blog/',views.blog,name='blog'),


]