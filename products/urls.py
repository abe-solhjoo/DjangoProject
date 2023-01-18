from django.urls import path
from products.views import ProductListView, ProductDetailView, ProductFeaturedDetailView, ProductFeaturedListView, \
    ProductDetailSlugView

app_name = "products"

urlpatterns = [
    path('', ProductListView.as_view(), name="list"),
    path('<slug>', ProductDetailSlugView.as_view(), name="detail"),

]
