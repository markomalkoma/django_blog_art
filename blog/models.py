from django.db import models
from django.contrib.auth.models import User 
from PIL import Image
from django.urls import reverse
from django.utils.timezone import now


# Create your models here.

class Post(models.Model):
    painting_name = models.CharField(max_length=100)
    painter = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    painting_image = models.ImageField(upload_to='cover_articles/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
    	return self.painting_name
    
    def get_absolute_url(self):
    	return reverse('post-detail', kwargs={'pk':self.pk})


class Comment(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
   
class Subcomment(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

   