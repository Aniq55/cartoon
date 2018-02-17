from django.conf.urls import url
from django.contrib import admin
from level import views

urlpatterns=[
	url(r'^$',views.index,name="index"),
	url(r'^page_1/$',views.page_1, name="page_1"),
	url(r'^page_2/$', views.page_2, name='page_2'),
	url(r'^leaderboard/$',views.leaderboard,name="leaderboard")
]