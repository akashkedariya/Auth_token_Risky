from django.urls import path
from accounts.views import UserLoginView, UserProfileView, UserRegistrationView,Demo,UserChangePasswordView,SendPasswordResetEmailView,UserPasswordResetView

urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('demo/',Demo.as_view(), name='demo'),
    path('change_password/',UserChangePasswordView.as_view(),name="change_password"),
    path('send_reset_password_email/', SendPasswordResetEmailView.as_view(),name="send_reset_password_email"),
    path('reset_password/<uid>/<token>/', UserPasswordResetView.as_view(),name="reset_password"),
]