from myapp.views import Postlist
from django.shortcuts import render
from rest_framework import generics # type: ignore
from .models import Postlist
from .serializers import Postlist
# Create your views here.


class Postlist(generics.ListCreateAPIView):
	queryset=Postlist.objects.all()
	serializer_class=PostlistSerializer

class Postlist(generics.RetrieveUpdateDestroyAPIView):
	queryset=Postlist
	serializer_class=PostlistSerializer

