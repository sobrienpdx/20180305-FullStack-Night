from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.utils import timezone 
from rest_framework.authtoken.models import Token

class Todo(models.Model):
    text = models.TextField()
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    edited_date = models.DateTimeField(blank=True, null=True) 

    class Meta:
        ordering = ['completed', '-created_date']   

    def __str__(self):
        return self.text 

    def save(self, *args, **kwargs):
        if not self.completed:
            self.edited_date = timezone.now()
        super(Todo, self).save(*args, **kwargs)


# For newly created users
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

