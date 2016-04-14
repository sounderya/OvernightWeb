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
    url(r'^signup/', 'news_analytics.views.signup'),
    url(r'^showBooking/', 'news_analytics.views.showBookingPage'),
    url(r'^showBookingConfirmation/', 'news_analytics.views.showBookingConfirmation'),
    url(r'^showUserProfile/', 'news_analytics.views.showUserProfile'),
    url(r'^showUserProfileBookingHistory/', 'news_analytics.views.showUserProfileBookingHistory'),
    url(r'^showUserProfileCards/', 'news_analytics.views.showUserProfileCards'),
    url(r'^showUserProfileSettings/', 'news_analytics.views.showUserProfileSettings')
)





