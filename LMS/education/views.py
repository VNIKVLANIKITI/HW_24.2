from rest_framework import viewsets, generics
from education.serializers import LessonSerializer, CourseSerializer
from education.models import lesson, course

# CRUD на вьюсетах
class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    queryset = lesson.objects.all()

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = course.objects.all()

# CRUD на дженериках
class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer

class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = lesson.objects.all()

class LessonRetriveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = lesson.objects.all()

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = lesson.objects.all()

class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = lesson.objects.all()