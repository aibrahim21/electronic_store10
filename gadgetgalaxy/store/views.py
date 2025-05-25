from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product, Category
from .forms import ProductForm

class ProductListView(ListView):
    model = Product
    template_name = 'store/product/list.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            queryset = queryset.filter(category=category)
        return queryset.filter(stock__gt=0)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['category'] = self.kwargs.get('category_slug')
        return context

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'store/product/form.html'
    success_url = reverse_lazy('store:product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'store/product/form.html'
    success_url = reverse_lazy('store:product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'store/product/confirm_delete.html'
    success_url = reverse_lazy('store:product_list')

def product_detail(request, id, slug):
    product = Product.objects.get(id=id, slug=slug)
    return render(request, 'store/product/detail.html', {'product': product})