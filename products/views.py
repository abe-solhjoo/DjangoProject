from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product
from django.http import Http404


class ProductFeaturedListView(ListView):
    template_name = "products/product_list.html"

    def get_queryset(self):
        return Product.objects.get_featured()


class ProductFeaturedDetailView(DetailView):
    template_name = "products/product_featured_detail.html"

    def get_queryset(self):
        return Product.objects.get_featured()


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/product_list.html"

    # def get_context_data(self, *args, object_list=None, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail_list.html"

    # def get_context_data(self,*args, object_list=None, **kwargs):
    #     context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context
    #

    def get_object(self, *args, **kwargs):
        request = self.request
        # print('test', request)
        productId = self.kwargs.get('pk')
        product = Product.objects.get_by_id(productId)
        if product is None:
            raise Http404('Product dose not found from custom model manager')
        return product
