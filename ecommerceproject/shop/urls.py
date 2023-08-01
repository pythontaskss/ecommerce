from . import views
from django.urls import path

app_name = 'shop'
urlpatterns = [
    # path('', views.demo, name='demo'),
    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodCatDetail'),
]
