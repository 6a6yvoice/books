from rest_framework.response import Response
from rest_framework.decorators import api_view,parser_classes
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

#@api_view(['GET'])
#@parser_classes([JSONParser])
#def example_view(request, format=None):
#    books = request.data('https://gitlab.grokhotov.ru/hr/yii-test-vacancy/-/raw/master/books.json')
#    return Response({'received data': request.data})