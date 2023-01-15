from django.urls import path
from products.views import ProductListView, ProductDetailView, ProductFeaturedDetailView, ProductFeaturedListView, \
    ProductDetailSlugView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('<slug>', ProductDetailSlugView.as_view(), name="ProductDetail"),

]
