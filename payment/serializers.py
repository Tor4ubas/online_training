from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from education.models import Course, Lesson
from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """ Сериализатор модели Payment """

    class Meta:
        model = Payment
        fields = "__all__"
