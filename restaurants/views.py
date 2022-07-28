import json

from django.db.models import Count, Avg
from django.http            import JsonResponse
from django.views           import View

from restaurants.models  import (
    Category,
    Restaurant,
    RestaurantImage,
    Menu
)
from users.models import (
    Like,
    Review
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

class RestaurantListView(View):
    def get(self,request):
        sort = request.GET.get('sort','id')

        FILTER_SET = {
            'category_id'     : 'category__in',
            'conformation_id' : 'conformation__in',
            'is_parking'      : 'is_parking'
        }

        SORT_SET = {
            'id'           : 'id',
            'random'       : '?',
            'low_rating'   : 'restaurant__review__rating',
            'high_rating'  : '-restaurant__review__rating',
        }

        q = {FILTER_SET.get(key) : json.loads(value) for key, value in request.GET.items() if key in FILTER_SET.keys()}

        restaurants = Restaurant.objects.filter(**q).order_by(SORT_SET[sort])

        results = [
            {   
                        'id'                   : restaurant.id,
                        'name'                 : restaurant.name,
                        'address'              : restaurant.address,
                        "category_id"          : restaurant.category.id,
                        "category_name"        : restaurant.category.name,
                        "is_parking"           : restaurant.is_parking,
                        'conformation_id'      : restaurant.conformation.id,
                        'conformation_content' : restaurant.conformation.content,
                        'rating'               : [
                            {
                                'rating' : review.rating
                        }for review in Review.objects.filter(restaurant_id=restaurant.id)],
                        'price'                : Menu.objects.filter(restaurant_id=restaurant.id).aggregate(Avg('price')),
                        'like'                 : Like.objects.filter(restaurant_id=restaurant.id).count(),
                         'image_url' : [
                            {
                                'id'  : image_url.id,
                                'url' : image_url.url,
                            } for image_url in RestaurantImage.objects.filter(restaurant_id=restaurant.id)
                        ]
            } for restaurant in restaurants
        ]
        return JsonResponse({'result' : results}, status = 200)
