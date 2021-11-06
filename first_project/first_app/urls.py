from django.urls import path

from first_app import views

urlpatterns = [
    # path("", views.home , name="home"),
    path("", views.index , name="index"),
    path('profile/', views.profile, name='profile'),
    path('page/', views.pageslist, name='page'),
    path('formpage/', views.formpage, name='formpage'),
]
