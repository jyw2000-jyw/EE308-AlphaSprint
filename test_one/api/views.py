from django.shortcuts import render
from api.models import api, name, times
from django.http import HttpResponse
import requests
import json

# def show(self, request):
#     result = api.objects.all()  # 获取对象
#     for u in result:
#         print(u.id, u.name, u.age, u.phone, u.addtime)
#     plays = []
#     for i in result:
#         plays.append({'id': i.id, 'name': i.name, 'point': i.point, 'bank': i.bank, 'help': i.help})
#     plays_json = json.dmps(plays, ensure_ascii=False)
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
    test = name.objects.get(user='i')
    id = test.name
    Allrepos_api_url = 'https://api.github.com/users/' +id+ '/repos?per_page=20'  # url拼接与解析
    headers = {"Authorization": "token " + "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"}  # token 增加请求次数
    requests.adapters.DEFAULT_RETRIES = 5  # 增加重试连接次数
    req = requests.get(Allrepos_api_url, headers=headers, timeout=(3, 7), auth=('admin', 'admin'))  # 防止timeout与身份验证的问题
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

        task = []
        # 显示所需数据
        for s in range(0, len(req_list1)):
            MyReposName = req_list1[s]['name']
            MyReposNames.append(MyReposName)

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
            task.append({'id': s, 'name': MyReposName, 'phone': MyReposDescription,'last':'-----(~.~)--------', 'created_at': MyReposCreatime, 'language': MyReposLanguage, 'watchers': MyReposWatchCount, 'watchers_count': MyReposStarCount})
            #, 'forks': MyReposForkCount,

        print('我的仓库名称：', MyReposNames,
              '\n我的仓库简介：', MyReposDescriptions,
              '\n我的仓库创建时间：', MyReposCreatimes,
              '\n我的仓库语言：', MyReposLanguages,
              '\n我的仓库watch数：', MyReposWatchCounts,
              '\n我的仓库star数：', MyReposStarCounts,
              '\n我的仓库fork数：', MyReposForkCounts,
              '\n我的仓库issue数：', MyReposIssueCounts)
        plays_json = json.dumps(task, ensure_ascii=False)
        return HttpResponse(plays_json)


def get(request):
    # phone = request.data.get('phone')
    # print(phone)
    # print(request.data)
    # print(request.query_params)
    print("ok")
    print(request.GET)
    a = request.GET.get('username')
    print(a)
    test = name.objects.get(user = 'i')
    test.name = a
    test.save()
    b = request.GET.get('password')
    print(b)

    # try:
    #     ob = api()
    #     print('yes')
    #     ob.name = a
    #     print('yes')
    #     ob.age = 1
    #     print('yes')
    #     ob.phone = b
    #     print('yes')
    #     ob.save()
    #     print('yes')
    # except:
    #     print('no')
    return HttpResponse("ok")



        # return Response({"status":True})

def test(request):
    test = name.objects.get(user='i')
    id = test.name
    Allrepos_api_url = 'https://api.github.com/users/' + id + '/repos?per_page=20'  # url拼接与解析
    headers = {"Authorization": "token " + "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"}  # token 增加请求次数
    requests.adapters.DEFAULT_RETRIES = 5  # 增加重试连接次数
    req = requests.get(Allrepos_api_url, headers=headers, timeout=(3, 10), auth=('admin', 'admin'))  # 防止timeout与身份验证的问题

    if req.status_code != 200:
        print(f'仓库获取请求出错！状态码：{req.status_code}!', req.json()['message'])
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
            MyReposNames.append(MyReposName)

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


        for i in range(0, len(MyReposNames)):

            MyRepo_commits_api_url = 'https://api.github.com/repos/' + 'jyw2000-jyw' + '/' + MyReposNames[
                i] + '/commits?per_page=10'  # 仓库commits情况url
            requests.adapters.DEFAULT_RETRIES = 5  # 增加重试连接次数
            req2 = requests.get(MyRepo_commits_api_url, headers=headers, timeout=(3, 10),
                                auth=('admin', 'admin'))  # 防止timeout与身份验证的问题
            req_list2 = req2.json()

            # 这里我删除了判断status_code，不然空库会返回409报错导致卡死（其实是我还不会改）
            commits = []
            for j in range(0, len(req_list2)):  # 按照时间最近到最早的顺序输出

                if type(req_list2) is dict:  # 增加这行防止出现空repo而报错
                    print(f'The Repository "{MyReposNames[i]}" is an empty repo!')
                    break
                else:
                    # print(f'\n用户"{id}"的仓库"{MyReposNames}"共有{len(req_list2)}次commits：\n')
                    Commiter = req_list2[j]['commit']['author']['name']
                    ModifyTime = req_list2[j]['commit']['author']['date'][:10]
                    ModifyAction = req_list2[j]['commit']['message']
                    commits.append({'commitNum': j + 1, 'change': Commiter, 'time': ModifyTime, 'move': ModifyAction})
            plays_json = json.dumps(commits, ensure_ascii=False)
            return HttpResponse(plays_json)
            #
            # return HttpResponse("ok")

def youwantcommit(request):
    # test = name.objects.get(user='i')
    # id = test.name
    # test.star = 0
    # test = name()
    # page = request.GET.get('pagenum')
    # print(page)
    # test.youwantnum = page
    commits = []
    test = name.objects.get(user='i')
    id = test.name
    star_api_url = 'https://api.github.com/users/' + id + '/starred?per_page=100'  # url拼接与解析
    headers = {"Authorization": "token " + "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"}  # token 增加请求次数
    requests.adapters.DEFAULT_RETRIES = 5  # 增加重试连接次数
    req = requests.get(star_api_url, headers=headers, timeout=(3, 10), auth=('admin', 'admin'))  # 防止timeout与身份验证的问题

    if req.status_code != 200:
        print(f'Star情况请求出错！状态码：{req.status_code}')
    else:
        req_list6 = req.json()

        StarRepoOwnerNames = []  # 我star的仓库的主人
        StarRepoNames = []  # 我star的仓库的名字
        StarReposLanguages = []  # 我star的仓库语言
        StarReposStarCounts = []  # 我star的仓库star数
        StarReposForkCounts = []  # 我star的仓库fork数
        StarReposIssueCounts = []  # 我star的仓库issue数

        for q in range(0, len(req_list6)):
            StarRepoOwnerName = req_list6[q]['owner']['login']
            StarRepoOwnerNames.append(StarRepoOwnerName)

            StarRepoName = req_list6[q]['name']
            StarRepoNames.append({'name':StarRepoName,'last':'-----s_s------'})

            StarReposLanguage = req_list6[q]['language']
            StarReposLanguages.append(StarReposLanguage)

            StarReposStarCount = req_list6[q]['stargazers_count']
            StarReposStarCounts.append(StarReposStarCount)

            StarReposForkCount = req_list6[q]['forks']
            StarReposForkCounts.append(StarReposForkCount)

            StarReposIssueCount = req_list6[q]['open_issues']
            StarReposIssueCounts.append(StarReposIssueCount)

        # print('我star的仓库拥有者：', StarRepoOwnerNames,
        #       '\n我star的仓库名：', StarRepoNames,
        #       '\n我star的仓库语言：', StarReposLanguages,
        #       '\n我star的仓库star数：', StarReposStarCounts,
        #       '\n我star的仓库fork数：', StarReposForkCounts,
        #       '\n我star的仓库issue数：', StarReposIssueCounts)
        # test.star = len(StarRepoNames)
        # test.save()
        play = json.dumps(StarRepoNames,ensure_ascii=False)
    return HttpResponse(play)

def pageget(request):#得到界面
    print("ok")
    print(request.GET)
    a = request.GET.get('pagenum')
    print(a)
    test = name.objects.get(user='i')
    test.page = a
    test.p = 1
    print(test.page)
    test.save()
    return HttpResponse("ok")


def commit(request):
    test = name.objects.get(user='i')
    id = test.name
    test.star = 0
    your_star = int(test.page) - 1
    commits = []
    star_api_url = 'https://api.github.com/users/' + id + '/starred?per_page=100'  # url拼接与解析
    headers = {"Authorization": "token " + "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"}  # token 增加请求次数
    requests.adapters.DEFAULT_RETRIES = 5  # 增加重试连接次数
    req = requests.get(star_api_url, headers=headers, timeout=(3, 10), auth=('admin', 'admin'))  # 防止timeout与身份验证的问题

    if req.status_code != 200:
        print(f'Star情况请求出错！状态码：{req.status_code}')
    else:
        req_list6 = req.json()

        StarRepoOwnerNames = []  # 我star的仓库的主人
        StarRepoNames = []  # 我star的仓库的名字
        StarReposLanguages = []  # 我star的仓库语言
        StarReposStarCounts = []  # 我star的仓库star数
        StarReposForkCounts = []  # 我star的仓库fork数
        StarReposIssueCounts = []  # 我star的仓库issue数



        for q in range(0, len(req_list6)):
            StarRepoOwnerName = req_list6[q]['owner']['login']
            StarRepoOwnerNames.append(StarRepoOwnerName)

            StarRepoName = req_list6[q]['name']
            StarRepoNames.append(StarRepoName)

            StarReposLanguage = req_list6[q]['language']
            StarReposLanguages.append(StarReposLanguage)

            StarReposStarCount = req_list6[q]['stargazers_count']
            StarReposStarCounts.append(StarReposStarCount)

            StarReposForkCount = req_list6[q]['forks']
            StarReposForkCounts.append(StarReposForkCount)

            StarReposIssueCount = req_list6[q]['open_issues']
            StarReposIssueCounts.append(StarReposIssueCount)

        # print('我star的仓库拥有者：', StarRepoOwnerNames,
        #       '\n我star的仓库名：', StarRepoNames,
        #       '\n我star的仓库语言：', StarReposLanguages,
        #       '\n我star的仓库star数：', StarReposStarCounts,
        #       '\n我star的仓库fork数：', StarReposForkCounts,
        #       '\n我star的仓库issue数：', StarReposIssueCounts)
        test.star = len(StarRepoNames)
        nownum = 0
        for i in range(0, len(StarRepoOwnerNames)):
            if i > your_star:
                break
            StarRepo_commits_api_url = 'https://api.github.com/repos/' + StarRepoOwnerNames[i] + '/' + StarRepoNames[
                i] + '/commits?per_page=10'  # 仓库commits情况url
            requests.adapters.DEFAULT_RETRIES = 5  # 增加重试连接次数
            req2 = requests.get(StarRepo_commits_api_url, headers=headers, timeout=(3, 10),
                                auth=('admin', 'admin'))  # 防止timeout与身份验证的问题
            req_list2 = req2.json()

            # 这里我删除了判断status_code，不然空库会返回409报错导致卡死（其实是我还不会改）
            changenum = 0
            nownum = len(req_list2)
            if i == your_star:
                tempnum = (i + 1)
                num = times.objects.get(name=tempnum)
                beforenum = int(num.times)
                changenum = nownum - beforenum
                print(beforenum,nownum,changenum)
            for j in range(0, len(req_list2)):  # 按照时间最近到最早的顺序输出
                Commiter = req_list2[j]['commit']['author']['name']
                ModifyTime = req_list2[j]['commit']['author']['date'][:10]
                ModifyAction = req_list2[j]['commit']['message']
                showchange = ''
                if j < changenum:
                    showchange = 'new'
                else:
                    showchange = 'old'
                if i == your_star:
                    commits.append({'commitNum': j + 1,'change':showchange, 'name': Commiter, 'time': ModifyTime, 'move': ModifyAction,'last':'------{^#^}-----'})



        plays_json = json.dumps(commits,ensure_ascii=False)
        return HttpResponse(plays_json)
                    #CommitDict = {'commitNum': j + 1, '修改者': Commiter, '修改时间': ModifyTime, '修改动作': ModifyAction}
