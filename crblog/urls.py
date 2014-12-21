from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crblog.views.home', name='home'),
    # url(r'^crblog/', include('crblog.foo.urls')),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^myadmin/doc/', include('django.contrib.admindocs.urls')),
    
    # Uncomment the next line to enable the admin:
    url(r'^myadmin/', include(admin.site.urls)),
    
    url(r'^$', 'core.views.getArticles'),    
    url(r'^article_list/page/(?P<num>\d+)$', 'core.views.getArticles'),
    url(r'^article/(\w+)$', 'core.views.getArticlesBySlug'),
    url(r'^article/tag/(\w+)/page/(\d+)$', 'core.views.getArticlesByTag'),
    url(r'^article/category/(\w+)/page/(\d+)$', 'core.views.getArticlesByCategory'),
    url(r'^test$', 'core.views.test'),
)