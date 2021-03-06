from django.urls import path, re_path
from basic_app import views

app_name = 'basic_app'

urlpatterns =[
    path('', views.SchoolListView.as_view(), name='list'),
    re_path(r'^(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(), name='detail'),
    # url(r'^P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(), name='detail'),
]