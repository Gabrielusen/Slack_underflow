from .models import PostQuestion
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostQuestion
        fields = '__all__'
