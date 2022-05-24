from rest_framework import serializers
from .models import *

class echarts_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = echarts_user
        fields = '__all__'