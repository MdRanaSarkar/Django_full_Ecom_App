from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from EcomApp.models import Setting, ContactMessage, ContactForm
from django.contrib import messages
from Product.models import Product, Images, Category, Comment
from EcomApp.forms import SearchForm
# Create your views here.
from OrderApp.models import ShopCart


def Home(request):
    current_user = request.user
    cart_product = ShopCart.objects.filter(user_id=current_user.id)
    total_amount = 0
    for p in cart_product:
        total_amount += p.product.new_price*p.quantity
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    sliding_images = Product.objects.all().order_by('id')[:2]
    latest_products = Product.objects.all().order_by('-id')
    products = Product.objects.all()
    total_quan = 0
    for p in cart_product:
        total_quan += p.quantity

    context = {'category': category,
               'setting': setting,
               'sliding_images': sliding_images,
               'latest_products': latest_products,
               'products': products,
               'cart_product': cart_product,
               'total_amount': total_amount,
               'total_quan': total_quan
               }
    return render(request, 'home.html', context)


def About(request):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    context = {'setting': setting,
               'category': category, }
    return render(request, 'about.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, 'Profile details updated.')

            return redirect('contact_dat')

    setting = Setting.objects.get(pk=1)
    form = ContactForm
    category = Category.objects.all()
    context = {
        'setting': setting, 'form': form, 'category': category,
    }
    return render(request, 'contact_form.html', context)


def SearchView(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            cat_id = form.cleaned_data['cat_id']
            if cat_id == 0:
                products = Product.objects.filter(title__icontains=query)
            else:
                products = Product.objects.filter(
                    title__icontains=query, category_id=cat_id)
            category = Category.objects.all()
            sliding_images = Product.objects.all().order_by('id')[:2]
            setting = Setting.objects.get(pk=1)
            context = {
                'category': category,
                'query': query,
                'product_cat': products,
                'sliding_images': sliding_images,
                'setting': setting,
            }
            return render(request, 'category_products.html', context)
    return HttpResponseRedirect('category_product')


def product_single(request, id):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    single_product = Product.objects.get(id=id)
    images = Images.objects.filter(product_id=id)
    products = Product.objects.all().order_by('id')[:4]
    comment_show = Comment.objects.filter(product_id=id, status='True')

    context = {
        'category': category,
        'setting': setting,
        'single_product': single_product,
        'images': images,
        'products': products,
        'comment_show': comment_show
    }
    return render(request, 'product-single.html', context)


def category_product(request, id, slug):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    sliding_images = Product.objects.all().order_by('id')[:2]
    prouct_cat = Product.objects.filter(category_id=id)
    context = {
        'category': category,
        'setting': setting,
        'product_cat': prouct_cat,
        'sliding_images': sliding_images,
    }
    return render(request, 'category_products.html', context)
