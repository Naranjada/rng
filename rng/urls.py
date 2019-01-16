from django.conf.urls import url
from django.contrib import admin
from elnombrequemasmeguste.views import IndexView
from . import views
from .views import TableListView
urlpatterns = [
	url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^admin/', admin.site.urls),
    url(r'^table/$', TableListView.as_view(), name="jugadoreslistview"),
    #url(r'^table/$', views.table),
    #url(r'^fixture/$', views.fixture),
]
