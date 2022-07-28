from django.urls import path
from restaurants.views import SearchView,CategoryView

urlpatterns = [
    path('/search',SearchView.as_view()),
    path('',CategoryView.as_view())
]