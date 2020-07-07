from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate, logout
from .forms import CustomerRegistrationForm, LoginForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)


def signup(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            username = authenticate(username=username, password=raw_password)
            login(request, username)
            return render(request, 'shop/product/list.html')
    else:
        form = CustomerRegistrationForm()

    return render(request, 'shop/cus_register.html', {'form': form})


class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = "shop/login.html"

    def valiadation(self):
        user = authenticate(username=username, password=raw_password)

        if user is not None:
            return product_list

        else:
            return signup
