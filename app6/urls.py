from django.urls import path
from.import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.user_login,name='login'),
    path('register/',views.register,name='register'),
    path('forgotpassword/',views.forgotpassword,name='forgotpassword'),
    path('resetpassword/',views.resetpassword,name='resetpassword'),
    path('product/',views.product,name='product'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('confirmation/',views.confirmation,name='confirmation'),
    path('checkout/',views.checkout,name='checkout'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update-cart/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('remove-item/<int:id>/', views.remove_item, name='remove_item'),
    

]