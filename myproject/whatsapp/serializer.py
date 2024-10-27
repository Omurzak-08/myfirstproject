from rest_framework import serializers
from .models import Task

class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created', ]