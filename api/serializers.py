from rest_framework import serializers
from .models import *


class HomeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    tags = serializers.StringRelatedField(many=True)
    class Meta:
        model=Project
        fields='__all__'
        # extra_kwargs = {
        #     # 'category': {'view_name': 'accounts', 'lookup_field': 'account_name'},
        #     'user': {'lookup_field': 'username'}
        # }
        


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = '__all__'
