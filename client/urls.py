from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('userDetails/', views.user_details, name="user_details"),
    path('profile/', views.profile, name="profile"),
    path('updateprofile/', views.update_profile, name="update_profile"),
    path('bid/<pk>', views.bid, name="bid"),
    path('productUpload/', views.productUpload, name="productUpload"),
    path('productView/<category>/', views.productView, name="productView"),
    path('contact/', views.contact, name="contact"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
