from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from goods import models

# Create your views here.


class goodsview(APIView):
    def get(self, request):
        models.LuckySpu.objects.all()


    def post(self, request):
        pass

class goodsdetail(APIView):
    def get(self, request):
        pass
    def put(self, request):
        pass
    def delete(self, request):
        pass