from django.urls import path

from shop import views

urlpatterns = [
    path('secure_view', views.secure_view),

    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),

    path('', views.Index.as_view(), name = 'index'),

    path('categories/', views.CategoryList.as_view(), name = 'categories'),
    path('category/<str:slug>', views.CategoryDetail.as_view(), name = 'category'),

    path('product/<int:pk>', views.ProductDetail.as_view(), name = 'product'),

    path('product/<int:product_id>/add_review/', views.ReviewCreate.as_view(), name = 'add_review'),
]