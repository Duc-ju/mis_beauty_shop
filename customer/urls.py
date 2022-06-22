from django.urls import path
from .views import UserAPIView, UpdateProfile, UserDetailAPIView

urlpatterns = [
    path('customers/', UserAPIView.as_view()),
    path('customers/<int:pk>/', UserDetailAPIView.as_view()),
    path('customers/<int:id>/profile/', UpdateProfile.as_view()),
]