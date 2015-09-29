from django.conf.urls import patterns, include, url
from omret.logreg import views as logreg_views
from omret import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'omret.views.home', name='home'),
    # url(r'^omret/', include('omret.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    #-------test-------
    #url(r'test/$',views.test),

    #----------logreg part ---------
    url(r'^signup/$',logreg_views.signup),
    #url(r'^login/$',logreg_views.login),
    url(r'^ver_signup/$',logreg_views.ver_signup),                      

    ##------the login view changed to home page now-------
    url(r'^$',logreg_views.login),
    url(r'^validatemail/',logreg_views.validatemail), 

    ##-------site is under building--------
    #url(r'^$',views.test),
)
