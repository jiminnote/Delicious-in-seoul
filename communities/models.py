from django.db import models

from core.models import TimeStampModel

# Create your models here.

class Community(TimeStampModel):   
    title    = models.CharField(max_length=15)
    user     = models.ForeignKey("users.User",on_delete=models.CASCADE)
    area     = models.ForeignKey("Area",on_delete=models.CASCADE)
    field    = models.ForeignKey("field",on_delete=models.CASCADE)
    category = models.ForeignKey("restaurants.Category",on_delete=models.CASCADE)
    content  = models.TextField()

    class Meta:
        db_table = 'communities'

class CommunityImage(models.Model):   
    comunnity = models.ForeignKey("Community",on_delete=models.CASCADE)
    url       = models.URLField()

    class Meta:
        db_table = 'community_images'

class Area(models.Model):   
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'areas'    

class Field(models.Model):   
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'fields'      

