from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name="home"),
    path("login", views.user_login,name="login"),
    path("signup", views.user_signup,name="signup"),
    path("otp_verification", views.otp_verification,name="otp_verification"),
    path("logout", views.user_logout,name="logout"),
    path("about_us", views.about_us,name="about_us"),
    path("contact_us", views.contact_us,name="contact_us"),
    path("profile", views.profile_page,name="profile"),
    path("track_order", views.track_order,name="track_order"),
    path("order1", views.order1,name="order1"),
    path("order2", views.order2,name="order2"),
    path("order3", views.order3,name="order3"),
    path("channel_integration", views.channel_integration,name="channel_integration"),
    path("carrier_integration", views.carrier_integration,name="carrier_integration"),
]

