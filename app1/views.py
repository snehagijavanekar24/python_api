from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET', 'POST'])
def First_view(request):
    msg='this is api'
    return Response(data={'msg':msg})

@api_view(['GET', 'POST','PUT','DELETE'])
def Second_view(request):
    if request.method == 'GET':
        msg='Get method work successfully'
    elif request.method == 'POST':
        msg='Post method work successfully'
    elif request.method == 'DELETE':
        msg='Delete method work successfully'
    return Response(data={'msg':msg})