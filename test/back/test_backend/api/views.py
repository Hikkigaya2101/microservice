from django.shortcuts import render
from .models  import *
from .serializer import *
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSeriliazer
    @action(methods=['GET'], detail=False)
    def get_tree(self,request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)