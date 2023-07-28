from rest_framework import serializers
from mysire.models import Contact

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__' 