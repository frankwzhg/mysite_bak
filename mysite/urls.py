from django.conf.urls import patterns, include, url
from django.contrib import admin
# from mysite.views import *
from books import views
# from contact.views import contact


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^hello/$', hello),
    # url(r'^time/$', current_datetime),
    # url(r'^time/plus/(\d{1,2})/$', hour_ahead),
    # url(r'^search-form/$', views.search_form),
    # url(r'^search/$', views.search),
    # url(r'^contact/$', contact)

)

urlpatterns += patterns('mysite.views',
                        url(r'^hello/$', 'hello'),
                        url(r'^time/$', 'current_datetime'),
                        url(r'^time/plus/(\d{1,2})/$', 'hour_ahead'),

                        )

urlpatterns += patterns('contact.views',
                        url(r'^contact/$', 'contact')
                        )
