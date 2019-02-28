from django.conf.urls import  patterns ,include, url
from django.views.generic.base import RedirectView
from django.contrib import admin
#admin.autodiscover()
from web01 import views
urlpatterns = patterns('',
	#url(r'^scp/$',views.SCP),
	#url(r'^updata/$',views.UPDATA),
	url(r'^login/$',views.login),
	url(r'^addhost/$',views.ADD_HOST),
	url(r'^test/$',views.TEXT),
	url(r'^index/$',views.INDEX),
	#url(r'^web/favicon.ico$',RedirectView.as_view(url=r'static/favicon.ico')),
	#url(r'^add/(?P<filename>\w*)/(?P<filepath>\w*)/$',views.model_add),
	url(r'^alllist/(\d+)*',views.show_web_asset),
	url(r'^mass_addhost/',views.TEXT),
	url(r'^deletehost/',views.delete_hosts),
	url(r'^deleteone/',views.delete_one),
	#url(r'^update_hostid/',views.update_hostid),
        url(r'^update_hostid/',views.update_hostid),
	#url(r'^gameplat/',views.GamePlat),
	#url(r'^register/',views.GameProject_Register),
	url(r'^ziban/',views.ziban),
	url(r'^mass_addhost2/',views.TEXT),
	url(r'^zhanshi/(\w+)*/(\d+)*/(\d+)*',views.zhanshi),
	url(r'^search/(\d+)*',views.SEARCH),
	#url(r'^ss/',views.get_all_host),
    url(r'^tree/(\d.+)*/(\d+)*',views.tree),

)
