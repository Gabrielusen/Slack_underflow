from rest_framework import serializers
from ..models import PostQuestion


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostQuestion
        fields = ('id', 'title', 'created_on', 'text_content')
