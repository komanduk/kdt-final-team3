from django.db import models
from django.conf import settings

# Create your models here.

class Post_bootscamp(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_users')


class Post_community(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title  = models.CharField(max_length=100)
    content = models.TextField()

class Comment(models.Model):
    post = models.ForeignKey(Post_community, on_delete=models.CASCADE, related_name='comment')
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)


class Post_image(models.Model):
    post = models.ForeignKey(Post_bootscamp, on_delete=models.CASCADE, related_name='post_image')
    post_image = models.ImageField(upload_to='post_image', blank=True, null=True)
    community_post = models.ForeignKey(Post_community, on_delete=models.CASCADE)
    community_image = models.ImageField(upload_to='community_image', blank=True, null=True)