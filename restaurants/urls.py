from django.urls import path
from restaurants.views import SearchView,RestaurantDetailView,CategoryView

urlpatterns = [
    path('/search',SearchView.as_view()),
    path('',CategoryView.as_view()),
    path('/<int:restaurant_id>',RestaurantDetailView.as_view())
    ]
