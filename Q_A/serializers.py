from rest_framework import serializers
from .models import questions

class questionSerializer(serializers.ModelSerializer):
    class Meta:
        model = questions
        fields = ['id','question']