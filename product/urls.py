from django.urls import include,path

from product import views


urlpatterns = [
path('newproducts/',views.newProductList.as_view()),
path('products/<slug:category_slug>/<slug:product_slug>/',views.ProductDetails.as_view()),
path('products/<slug:category_slug>/',views.CategoryDetail.as_view()),
path('products/search',views.search)
]