from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView
from . models import Items
from . serilaizers import ItemSerializer
# Create your views here.
class ItemListCreateView(ListCreateAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer
    
class ItemDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer