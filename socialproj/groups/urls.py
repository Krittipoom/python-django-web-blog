#urls.py
from django.conf.urls import url
from . import views

app_name = 'groups'

urlpatterns = [
	path('', views.ListGroups.as_view(), name = 'all'),
	path('new/', views.CreateGroups.as_view(), name = 'create'),
	path('posts/in/<slug:slug>/', views.SingleGroups.as_view(), name = 'single'),
	path('join/<slug:slug>/', views.JoinGroups.as_view(), name = 'join'),
	path('leave/<slug:slug>/', views.LeaveGroups.as_view(), name = 'leave'),
]