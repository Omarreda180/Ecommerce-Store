from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('store/', views.store, name='store'),
    path('store/<slug:category_slug>/', views.store, name='products_by_categries'),
    path('store/<slug:category_slug>/<slug:product_details_slug>/', views.product_details, name='product_details'),
    path('search/', views.search, name='search'),
    path('review/<int:product_id>/', views.review, name='review'),
]
