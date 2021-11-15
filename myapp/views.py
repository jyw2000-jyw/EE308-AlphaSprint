from django.shortcuts import render
from django.http import HttpResponse
# from rest_framework.views import APIView    
#from rest_framework.response import Response


# class LoginView(APIView):
def get(request):
    # phone = request.data.get('phone')
    # print(phone)
    # print(request.data)
    #print(request.query_params)
    
    print(request.GET)
    a = request.GET.get('phone')
    print(a)
    b = request.GET.get('code')
    print(b)
    return HttpResponse("ok")
# Create your views here.
