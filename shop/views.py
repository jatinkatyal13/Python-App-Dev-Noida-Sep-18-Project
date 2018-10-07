from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator

from shop import models, forms

# Create your views here.

@login_required
def secure_view(request):
    return HttpResponse("You are authenticated")

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('index'))

    if request.method == "GET":
        form = forms.LoginForm()
    elif request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user:
                auth_login(request, user)
                return HttpResponseRedirect(reverse_lazy('index'))

    context = {
        'form': form
    }
    return render(request, 'shop/login.html', context)

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse_lazy('index'))

@method_decorator(login_required, name='dispatch')
class Index(TemplateView):
    template_name = 'shop/index.html'

    # @login_required
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(self, *args, **kwargs)

class CategoryList(ListView):
    model = models.Category
    # template_name = ''
    # context_object_name = ''

# def category_list(request):
#     categories = models.Category.objects.all()
#     context = {
#         "object_list": categories
#     }
#     return render(request, 'shop/category_list.html', context)

class CategoryDetail(DetailView):
    model = models.Category

# def category_detail(request, slug):
#     category = models.Category.object.get(slug = slug)

#     context = {
#         "object": category,
#     }
#     return render(request, 'shop/category_detail.html', context)

class ProductDetail(DetailView):
    model = models.Product

class ReviewCreate(CreateView):
    model = models.Review
    fields = ('content', 'author')

    def form_valid(self, form):
        product = models.Product.objects.get(id = self.kwargs['product_id'])
        obj = form.save(commit = False) # create object in memory
        obj.product = product # adding missing data
        obj.save() # hitting the db

        success_url = reverse_lazy('product', kwargs = {"pk":product.id})

        return HttpResponseRedirect(success_url)

# def add_review(request, product_id):
#     if request.method == "GET":
#         form = ReviewForm()
#     elif request.method == "POST":
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             product = models.Product.objects.get(id = product_id)
#             # obj = models.Review.objects.create(
#             #     product = product,
#             #     content = form.cleaned_data['content'],
#             #     author = form.cleaned_data['author']
#             # )

#             # obj = models.Review(
#             #     content = form.cleaned_data['content'],
#             #     author = form.cleaned_data['author']
#             # )
#             # obj.product = product
#             # obj.save()

#             obj = form.save(commit = False)
#             obj.product = product
#             obj.save()

#     context = {
#         'form': form
#     }
#     return render(request, 'shop/review_form.html', context)

