from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [
	url(r'^$', views.main, name="main"),
	url(r'^admin/', admin.site.urls),
]
#ec2-13-125-213-98.ap-northeast-2.compute.amazonaws.com