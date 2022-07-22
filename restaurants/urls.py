from django.urls import path
from restaurants.views import SearchView

urlpatterns = [
    path('',SearchView.as_view())
]