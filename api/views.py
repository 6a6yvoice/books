from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ItemSerializer
from mysire.models import Contact
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView


@api_view(['GET'])
def getData(request):
    contacts = Contact.objects.all()
    serializer = ItemSerializer(contacts, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request): 
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
