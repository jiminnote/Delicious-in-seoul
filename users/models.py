from django.db import models

from core.models import TimeStampModel

# Create your models here.
class User(TimeStampModel):   
    email         = models.CharField(max_length = 45,unique = True,null=True)
    kakao_id      = models.BigIntegerField(unique = True, null=True)
    nickname      = models.CharField(max_length = 20,unique = True)
    profile_image = models.URLField(null=True)
    password      = models.CharField(max_length = 100)
    category      = models.ForeignKey("restaurants.Category",on_delete = models.CASCADE)

    class Meta:
        db_table = 'users'

class Review(TimeStampModel):   
    user       = models.ForeignKey("User",on_delete = models.CASCADE)
    restaurant = models.ForeignKey("restaurants.Restaurant",on_delete = models.CASCADE)
    contents   = models.TextField()
    rating     = models.IntegerField()
    
    class Meta:
        db_table = 'reviews'

class ReviewImage(TimeStampModel):   
    review = models.ForeignKey("Review",on_delete = models.CASCADE)
    url    = models.URLField()
    
    class Meta:
        db_table = 'review_images'
        
class Chat(TimeStampModel):   
    user   = models.ForeignKey("User",on_delete = models.CASCADE)
    chat_list  = models.ForeignKey("ChatList",on_delete = models.CASCADE)
    is_from_sender = models.BooleanField(default=False)
    content = models.TextField()
    read =  models.BooleanField(default=False)
    send_message_time = models.TimeField()

    class Meta:
        db_table = 'chats'

class ChatList(TimeStampModel):   
    user              = models.ForeignKey("User",on_delete = models.CASCADE)
    from_user         = models.ForeignKey("User",related_name='from_id',on_delete = models.CASCADE)
    to_user           = models.ForeignKey("User",related_name='to_id',on_delete = models.CASCADE)
    content           = models.TextField()
    last_message      = models.CharField(max_length=225)
    who_is_last       = models.CharField(max_length=225)
    last_message_time = models.TimeField()

    class Meta:
        db_table = 'chat_lists'

class Like(TimeStampModel):   
    user       = models.ForeignKey("User",on_delete = models.CASCADE)
    restaurant = models.ForeignKey("restaurants.Restaurant",on_delete = models.CASCADE,null=True)
    community  = models.ForeignKey("communities.Community",on_delete = models.CASCADE,null=True)
    review     = models.ForeignKey("Review",on_delete = models.CASCADE,null=True)

    class Meta:
        db_table = 'likes'

class Comment(TimeStampModel):   
    user              = models.ForeignKey("User",on_delete = models.CASCADE)
    restaurant        = models.ForeignKey("restaurants.Restaurant",on_delete = models.CASCADE,null=True)
    community         = models.ForeignKey("communities.Community",on_delete = models.CASCADE,null=True)
    review            = models.ForeignKey("Review",on_delete = models.CASCADE,null=True)
    parent_comment_id = models.ForeignKey("self",on_delete = models.CASCADE,null=True)
    content           = models.TextField()

    class Meta:
        db_table = 'comments'

class Hit(TimeStampModel):   
    user       = models.ForeignKey("User",on_delete = models.CASCADE)
    restaurant = models.ForeignKey("restaurants.Restaurant",on_delete = models.CASCADE,null=True)
    community  = models.ForeignKey("communities.Community",on_delete = models.CASCADE,null=True)
    review     = models.ForeignKey("Review",on_delete = models.CASCADE,null=True)
 
    class Meta:
        db_table = 'hits'


