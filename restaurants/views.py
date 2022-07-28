
import json
from django.db.models import Count

from django.http            import JsonResponse
from django.views           import View

from restaurants.models   import (
    Category,
    MainCategory,
    Restaurant
)
# Create your views here.
class SearchView(View):
    def get(self,request):
        categories = Category.objects.filter(id__in=[1,2,3,4])

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

class CategoryView(View):
    def get(self,request):
        main_categories = MainCategory.objects.all()
        categories = Category.objects.all()
        results = [
                    {   
                        'id'     : main_category.id,
                        'name'   : main_category.name,
                        'restaurants' : [
                            {
                                'id'     : category.id,
                                'name'   : category.name,
                            } for category in categories.filter(main_category_id=main_category.id)
                        ]
                        }for main_category in main_categories
                    ]
        return JsonResponse({'result' : results}, status = 200)
