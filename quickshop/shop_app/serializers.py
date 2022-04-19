from rest_framework import serializers
from . models import Quickshop

class QuickshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quickshop
        fields = "__all__"