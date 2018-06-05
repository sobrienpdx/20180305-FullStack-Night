from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class BlogPost(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	body = models.TextField()
	timestamp = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title


class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
	body = models.CharField(max_length=500)
	timestamp = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.body
