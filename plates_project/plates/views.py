from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse

from .models import Plate
from .serializers import PlateSerializer

from rest_framework import mixins

from rest_framework import status
from rest_framework.decorators import api_view  # Импортировали декоратор
from rest_framework.response import Response

from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class PlateGetViewSet(viewsets.ModelViewSet):
    queryset = Plate.objects.all()
    serializer_class = PlateSerializer


class PlateAddViewSet(viewsets.ModelViewSet):
    queryset = Plate.objects.all()
    serializer_class = PlateSerializer

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save()
