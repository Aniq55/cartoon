from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^',include('level.urls')),	
	#url(r'^level/page_1/$',views.page_1,name="page_1"),
	 url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^auth/', include('social_django.urls', namespace='social')), 

]
