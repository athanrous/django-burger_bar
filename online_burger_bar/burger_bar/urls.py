from django.conf.urls import url
from django.conf import settings

#from . import views
from burger_bar import views
from django.conf.urls.static import static


urlpatterns = [
	url(r'^$', views.product_list, name='product_list'),
	url(r'^(?P<category_slug>[-\w]+)/$',views.product_list,name='product_list_by_category'),
	url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.product_detail,name='product_detail'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

