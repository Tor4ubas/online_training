from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import viewsets

from education.models import Course, Lesson
from education.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """ Простой ViewSet-класс для вывода информации """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonListAPIView(ListAPIView):
    """ Отвечает за отображение списка сущностей (Generic-класс)"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(RetrieveAPIView):
    """ Отвечает за отображение одной сущности (Generic-класс)"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonCreateAPIView(CreateAPIView):
    """ Отвечает за создание сущности (Generic-класс)"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(UpdateAPIView):
    """ Отвечает за редактирование сущности (Generic-класс)"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(DestroyAPIView):
    """ Отвечает за удаление сущности (Generic-класс)"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
