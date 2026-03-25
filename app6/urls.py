from django.urls import path
from.import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.user_login,name='login'),
    path('register/',views.register,name='register'),
    path('forgotpassword/',views.forgotpassword,name='forgotpassword'),
    path('resetpassword/',views.resetpassword,name='resetpassword'),
    path('shopingcart/',views.shopingcart,name='shopingcart'),
    path('product/',views.product,name='product'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('confirmation/',views.confirmation,name='confirmation'),
    path('checkout/',views.checkout,name='checkout'),
]