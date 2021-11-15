from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import api
from django.http import HttpResponse
import  json


# def show(self, request):
#     result = api.objects.all()  # 获取对象
#     for u in result:
#         print(u.id, u.name, u.age, u.phone, u.addtime)
#     plays = []
#     for i in result:
#         plays.append({'id': i.id, 'name': i.name, 'point': i.point, 'bank': i.bank, 'help': i.help})
#     plays_json = json.dumps(plays, ensure_ascii=False)
#     return HttpResponse(plays_json)  # 转换为json格式




def insertUsers(request):
    try:
        ob = api()
        ob.name = request.POST['phone']
        ob.age = request.POST['code']
        ob.phone = request.POST['phone']
        ob.save()
        context = {'info':'添加成功！'}
    except:
        context = {'info':'添加失败！'}
    return render(request,"myapp/api/info.html",context)

class LoginView(APIView):
    def get(self, request, *args, **kwargs):
        # phone = request.data.get('phone')
        # print(phone)
        # print(request.data)
        #print(request.query_params)
        phone = request.query_params.get('phone')
        code = request.query_params.get('code')
        print(phone, "(^-^) ", code)

        try:
            ob = api()
            print('yes')
            ob.name = code
            print('yes')
            ob.age = 1
            print('yes')
            ob.phone = phone
            print('yes')
            ob.save()
            print('yes')
        except:
            print('no')

        return Response({"status":True})
