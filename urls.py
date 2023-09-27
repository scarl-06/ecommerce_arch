from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.user_registration, name='register'),
    path('login/', views.user_login, name='login'),
    path('checkout/', views.checkout, name='checkout'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    # Define other URL patterns for your app here
]
 