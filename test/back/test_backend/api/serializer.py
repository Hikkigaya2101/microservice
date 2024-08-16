from rest_framework import serializers
from .models import *

class UnitSeriliazer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(slug_field='name',read_only=True)
    class Meta:
        model = Unit
        fields = '__all__'