# products/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.contrib.auth.decorators import login_required
from django.db.models import Q # Used for search functionality

from .models import Product, Category, Order
from .serializers import ProductSerializer, UserSerializer, CategorySerializer, OrderSerializer
from .forms import UserRegisterForm, ProductForm, ProfileUpdateForm # Make sure all forms are imported here

# Frontend Views (for rendering HTML templates)
def home_view(request):
    """
    Renders the homepage.
    """
    return render(request, 'home.html')

def product_grid_view(request):
    """
    Renders the product grid page with search functionality.
    """
    products = Product.objects.all()
    search_query = request.GET.get('search', '') # Get the search query from the URL

    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(category__name__icontains=search_query)
        )
        
    context = {'products': products, 'search_query': search_query}
    return render(request, 'product_grid.html', context)

def product_detail_view(request, pk):
    """
    Renders a single product detail page.
    """
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context)
    
def category_list_view(request):
    """
    Renders the category list page.
    """
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'category_list.html', context)
    
def category_detail_view(request, pk):
    """
    Renders a single category detail page.
    """
    category = get_object_or_404(Category, pk=pk)
    context = {'category': category}
    return render(request, 'category_detail.html', context)
    
@login_required
def order_list_view(request):
    """
    Renders the order list page for the authenticated user.
    """
    orders = Order.objects.filter(user=request.user)
    context = {'orders': orders}
    return render(request, 'order_list.html', context)
    
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login.html', context)

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'register.html', context)

def logout_view(request):
    auth_logout(request)
    return redirect('home')
    
@login_required
def product_edit_view(request, pk):
    """
    Renders the product edit page and handles form submission.
    """
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    
    context = {'form': form, 'product': product}
    return render(request, 'product_edit.html', context)

@login_required
def product_create_view(request):
    """
    Renders the product creation page and handles form submission.
    """
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products-grid')
    else:
        form = ProductForm()
    
    context = {'form': form}
    return render(request, 'product_create.html', context)

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileUpdateForm(instance=request.user)
    
    context = {'form': form}
    return render(request, 'profile.html', context)

# API ViewSets for DRF (for RESTful endpoints)
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category']
    search_fields = ['name', 'category__name']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticatedOrReadOnly()]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        
        in_stock = self.request.query_params.get('in_stock')
        if in_stock == 'true':
            queryset = queryset.filter(stock_quantity__gt=0)
        elif in_stock == 'false':
            queryset = queryset.filter(stock_quantity=0)
        
        return queryset

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticated()]
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)