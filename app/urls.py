from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name="home"),
    path('my-dashboard',views.dashboard, name="dashboard"),
    path('products/',views.products, name="products"),
    path('signup',views.signup, name="signup"),
    path('signin',views.signin, name="signin"),
    path('logout',views.logout_user, name="logout"),
    path('single-product/<slug>/',views.single_product, name="single_product"),
    path('cart',views.p_cart, name="cart"),
    path('add-to-cart/<slug>',views.add_to_cart, name="add_to_cart"),
    path('remove-from-cart/<slug>', views.remove_from_cart, name="remove_from_cart"),
    path('checkout',views.checkout, name="checkout"),
    path('order',views.order, name="order"),
    path('place-order',views.place_order, name="place_order"),
    path('profile-details',views.profile_details, name="profile_details"),
    path('profile-details-update',views.profile_details_update, name="profile_details_update"),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', views.activate, name='activate'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

