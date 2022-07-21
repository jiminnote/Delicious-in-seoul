from django.db import models

from core.models import TimeStampModel

# Create your models here.
class MainCategory(models.Model):   
    name = models.CharField(max_length=15)
    
    class Meta:
        db_table = 'main_categories'

class Category(models.Model):   
    name          = models.CharField(max_length=15)
    main_category = models.ForeignKey("MainCategory",on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

class Restaurant(TimeStampModel):
    category          = models.ForeignKey("Category",on_delete=models.CASCADE)
    conformation      = models.ForeignKey("Conformation",on_delete=models.CASCADE)
    information       = models.CharField(max_length=50,null=True)
    name              = models.CharField(max_length=50)
    is_parking        = models.BooleanField(default=False)
    road_name_address = models.CharField(max_length=255)
    address           = models.CharField(max_length=255)
    phone_number      = models.CharField(max_length=20)
    open_time         = models.CharField(max_length=20,null=True)
    break_time        = models.CharField(max_length=20,null=True)
    day_off           = models.CharField(max_length=20,null=True)
    url               = models.URLField()
    latitude          = models.DecimalField(max_digits=20, decimal_places=14, default=0.0)
    longitude         = models.DecimalField(max_digits=20, decimal_places=14, default=0.0)

    class Meta:
        db_table = 'restaurants'

class Conformation(models.Model):
    content = models.CharField(max_length=50)

    class Meta:
        db_table = 'conformations'

class menus(models.Model):
    name       = models.CharField(max_length=255)
    restaurant = models.ForeignKey("Restaurant",on_delete=models.CASCADE)
    price      = models.DecimalField(max_digits = 15, decimal_places = 3)

    class Meta:
        db_table = 'menus'

class RestaurantImage(models.Model):
    restaurant = models.ForeignKey("Restaurant",on_delete=models.CASCADE)
    url        = models.URLField()

    class Meta:
        db_table = 'restaurant_images'
