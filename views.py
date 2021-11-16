from django.shortcuts import render
from api.models import api
from django.http import HttpResponse
import requests
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


def userInfo(request):
    Allrepos_api_url = 'https://api.github.com/users/' +'jyw2000-jyw'+ '/repos?per_page=20'  # url拼接与解析
    headers = {"Authorization": "token " + "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"}  # token 增加请求次数
    req = requests.get(Allrepos_api_url, headers=headers)
    if req.status_code != 200:
        print(f'仓库获取请求出错！状态码：{req.status_code}')
    else:
        req_list1 = req.json()

        print(f'请求成功！状态码：{req.status_code}')

        print(f'用户"{id}"有{len(req_list1)}个仓库：\n')

        MyReposNames = []  # 我的仓库名称
        MyReposDescriptions = []  # 我的仓库简介
        MyReposCreatimes = []  # 我的仓库创建时间
        MyReposLanguages = []  # 我的仓库语言
        MyReposWatchCounts = []  # 我的仓库watch数
        MyReposStarCounts = []  # 我的仓库star数
        MyReposForkCounts = []  # 我的仓库fork数
        MyReposIssueCounts = []  # 我的仓库issue数

        # 显示所需数据
        for s in range(0, len(req_list1)):
            MyReposName = req_list1[s]['name']
            MyReposNames.append({'id':s,'name': MyReposName,'phone':'(^0^)'})

            MyReposDescription = req_list1[s]['description']
            MyReposDescriptions.append(MyReposDescription)

            MyReposCreatime = req_list1[s]['created_at']
            MyReposCreatimes.append(MyReposCreatime)

            MyReposLanguage = req_list1[s]['language']
            MyReposLanguages.append(MyReposLanguage)

            MyReposWatchCount = req_list1[s]['watchers']
            MyReposWatchCounts.append(MyReposWatchCount)

            MyReposStarCount = req_list1[s]['watchers_count']
            MyReposStarCounts.append(MyReposStarCount)

            MyReposForkCount = req_list1[s]['forks']
            MyReposForkCounts.append(MyReposForkCount)

            MyReposIssueCount = req_list1[s]['open_issues']
            MyReposIssueCounts.append(MyReposIssueCount)

        print(#'我的仓库名称：', MyReposNames,
              '\n我的仓库简介：', MyReposDescriptions,
              '\n我的仓库创建时间：', MyReposCreatimes,
              '\n我的仓库语言：', MyReposLanguages,
              '\n我的仓库watch数：', MyReposWatchCounts,
              '\n我的仓库star数：', MyReposStarCounts,
              '\n我的仓库fork数：', MyReposForkCounts,
              '\n我的仓库issue数：', MyReposIssueCounts)
        plays_json = json.dumps(MyReposNames, ensure_ascii=False)
        return HttpResponse(plays_json)

def get(request):
    # phone = request.data.get('phone')
    # print(phone)
    # print(request.data)
    # print(request.query_params)

    print(request.GET)
    a = request.GET.get('phone')
    print(a)
    b = request.GET.get('code')
    print(b)
    try:
        ob = api()
        print('yes')
        ob.name = a
        print('yes')
        ob.age = 1
        print('yes')
        ob.phone = b
        print('yes')
        ob.save()
        print('yes')
    except:
        print('no')
    return HttpResponse("ok")



        # return Response({"status":True})
