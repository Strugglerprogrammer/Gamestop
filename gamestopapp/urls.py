from django.urls import path
from gamestopapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index,),
    path('create_product', views.create_product,),
    path('read_product', views.read_product),
    path('update_product/<rid>', views.update_product),
    path('delete_product/<rid>', views.delete_product),
    path('register', views.user_register),
    path('login', views.user_login),
    path('logout', views.user_logout),
    path('create_cart/<rid>', views.create_cart)
]


urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)