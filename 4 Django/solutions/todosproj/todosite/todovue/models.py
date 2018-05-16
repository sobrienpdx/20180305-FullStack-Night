from django.db import models
from django.utils import timezone 

class Todo(models.Model):
	text = models.TextField()
	completed = models.BooleanField(default=False)
	created_date = models.DateTimeField(default=timezone.now)
	edited_date = models.DateTimeField(blank=True, null=True) 

	def __str__(self):
		return self.text 

	def toggle_completed(self):
		self.completed = not self.completed
		self.edited_date = timezone.now()
		self.save()

		