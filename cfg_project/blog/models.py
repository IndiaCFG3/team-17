from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100) #city
    Lane_name = models.TextField() #lane
    WasteIn = models.IntegerField(default=0)
    WasteOut = models.IntegerField(default=0)
    date_posted = models.DateTimeField(default=timezone.now) #auto_now records time of every update where as auto_now_add records just the time of creation
    #here now is a function but we pass the function so no parenthesis '()' as it executes the function
    author = models.ForeignKey(User, on_delete=models.CASCADE) #One to many from author to post | on_delete tells to delete all post of the user/author if he/she gets deleted
    #author->user
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})
