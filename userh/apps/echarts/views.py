from django.shortcuts import render
from rest_framework.response import Response

from django.views import View
from rest_framework.views import APIView
import os,sys
from .models import *
from .stsass import *
import json
# from rest_framework.views import APIView
class Show(APIView):
    def get(self, request):
        path = "C:\\Users\\longs\\Desktop\\user\\Blog\\userh\\apps\\echarts\\data\\"
        show_user = echarts_user.objects.all()
        title_json = []
        title_list = []
        for i in show_user:
            title_list.append(i.ec_name)
            path_json = json.load(open(path + i.ec_name +".json",'r',encoding='utf-8'))
            title_json.append(path_json)
            # titles.append(i.ec_name)
        title_json.append(title_list)
        return Response(title_json)
    def post():
        pass
