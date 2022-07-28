from tkinter import Menu
from django.db.models import Count
import json

from django.http            import JsonResponse
from django.views           import View
from my_settings import IMAGE_URL

from restaurants.models   import (
    Category,
    Restaurant,
    Menu,
    RestaurantImage
)
from users.models import (
    Like
)
# Create your views here.
class SearchView(View):
    def get(self,request):
        categories = Category.objects.filter(id__in=[1,2,3,4])
        #count = categories.aggregate(count=Count('id'))

        results = [
                    {   
                        'id'    : category.id,
                        'name'  : category.name,
                        'count' : category.restaurant_set.aggregate(count=Count('id')),
                        'restaurants' : [
                            {
                                'id'       : restaurant.id,
                                'name'     : restaurant.name,
                                'address'  : restaurant.address
                            } for restaurant in category.restaurant_set.all()
                        ]
                        }for category in categories.filter(id__lt=5)
                    ]
        return JsonResponse({'result' : results}, status = 200)
    
class RestaurantDetailView(View):
    def get(self,request,restaurant_id):
        restaurant = Restaurant.objects.get(id=restaurant_id)
        likes      =  Like.objects.filter(restaurant_id=restaurant_id)
        menus      =  Menu.objects.filter(restaurant_id=restaurant_id)
        image_urls =  RestaurantImage.objects.filter(restaurant_id=restaurant_id)

        results = {   
                        'id'                   : restaurant.id,
                        'name'                 : restaurant.name,
                        'address'              : restaurant.address,
                        "category_id"          : restaurant.category.id,
                        "category_name"        : restaurant.category.name,
                        'conformation_id'      : restaurant.conformation.id,
                        'conformation_content' : restaurant.conformation.content,
                        'like'                : likes.aggregate(count=Count('id')),
                        'memus' : [
                            {
                                'id'   : menu.id,
                                'name' : menu.name,
                            } for menu in menus
                        ],
                         'image_url' : [
                            {
                                'id'  : image_url.id,
                                'url' : image_url.url,
                            } for image_url in image_urls
                        ]
            }
        return JsonResponse({'result' : results}, status = 200)