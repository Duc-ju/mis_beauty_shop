from django.urls import path
from .views import AdviseAPIView

urlpatterns = [
    path('advise/', AdviseAPIView.as_view()),
]