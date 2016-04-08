from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'news_analytics.views.landing_page'),
    url(r'^get_news/', 'news_analytics.views.get_content'),
    url(r'^showResult/', 'news_analytics.views.showSearchresult'),
    url(r'^login/', 'news_analytics.views.login'),
    url(r'^signup/', 'news_analytics.views.signup')

)





