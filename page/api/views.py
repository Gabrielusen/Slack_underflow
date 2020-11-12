from rest_framework import generics
from ..models import PostQuestion
from .serializers import QuestionSerializer


class QuestionList(generics.ListAPIView):
    queryset = PostQuestion.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostQuestion.objects.all()
    serializer_class = QuestionSerializer
