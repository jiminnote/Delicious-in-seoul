from unicodedata import category
from django.shortcuts import render

# Create your views here.
import json

from django.http            import JsonResponse
from django.views           import View

from restaurants.models   import (
    Category,
    Restaurant
)
# Create your views here.
class SearchView(View):
    def get(self,request):
        categories = Category.objects.all()
        
        results = [
                    {   
                        'id'     : category.id,
                        'name'   : category.name,
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