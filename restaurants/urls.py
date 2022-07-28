from django.urls import path
from restaurants.views import SearchView,RestaurantDetailView

urlpatterns = [
    path('',SearchView.as_view()),
    path('/<int:restaurant_id>',RestaurantDetailView.as_view())
]