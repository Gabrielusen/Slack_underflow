from rest_framework import generics
from ..models import PostQuestion
from .serializers import QuestionSerializer


class QuestionList(generics.ListCreateAPIView):
    queryset = PostQuestion.objects.all()
    serializer_class = QuestionSerializer
