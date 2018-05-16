from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	text = serialzers.TextField()
	completed = serializers.BooleanField(default=False)
	created_date = serializers.DateTimeField(default=timezone.now)
	edited_date = serializers.DateTimeField(blank=True, null=True) 

	def create(self, validated_data):
		""" Create and return a new Todo instance given the validated data.
		"""
		return Todo.objects.create(**validated_data)

	def update(self, instance, validated_data):
		""" Update and return and existing Todo instance given the validated data.
		"""
		text
		completed
		edited_date
