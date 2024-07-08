from django.urls import path
from .views import IndexView  # Use relative import

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
