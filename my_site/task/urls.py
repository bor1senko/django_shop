from django.conf.urls import include, url

import views

urlpatterns = [
    url(r'^$', views.home_page),
    url(r'^cart$', views.cart),
    url(r'^catalog/(?P<option>[a-z]+)/(?P<product_id>[0-9]+)', views.product_view ),
    url(r'^category', views.category_view ),
    url(r'^search',views.search ),
]
