from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,ListAPIView
from . models import Items
from . serilaizers import ItemSerializer
# Create your views here.
class ItemListCreateView(ListCreateAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer