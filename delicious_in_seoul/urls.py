
from django.urls import path,include

urlpatterns = [
   path('user',include('users.urls')),
   path('restaurant',include('restaurants.urls')),
   path('community',include('communities.urls')),
]
