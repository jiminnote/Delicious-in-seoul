from django.urls import path
from restaurants.views import SearchView,RestaurantListView

urlpatterns = [
    path('',SearchView.as_view()),
    path('/list',RestaurantListView.as_view())
]