for m in range(0, len(StarRepoOwnerNames)):
    StarRepoBranches_url = 'https://api.github.com/repos/' + StarRepoOwnerNames[m] + '/' + StarRepoNames[
        m] + '/branches?per_page=10'  # 仓库branch情况url
    req2 = requests.get(StarRepoBranches_url)
    if req2.status_code != 200:
        print(f'star仓库branches情况请求出错！状态码：{req2.status_code}')
        break
    else:
        req_list2 = req2.json()

        StarRepoBranches = []  # 我star的仓库的branch
        StarRepoBranchesShas = []  # 我star的仓库的branch的sha地址

        for n in range(0, len(req_list2)):
            StarRepoBranch = req_list2[n]['name']
            StarRepoBranches.append(StarRepoBranch)

            StarRepoBranchesSha = req_list2[n]['commit']['sha']
            StarRepoBranchesShas.append(StarRepoBranchesSha)

        dic = {key: value for key, value in zip(StarRepoBranches, StarRepoBranchesShas)}
        print(dic)

        for key in dic.keys():
            for i in range(0, len(StarRepoOwnerNames), len(StarRepoOwnerNames)):  # 此处要设置步长（重点）
                StarRepoBranch_commits_api_url = 'https://api.github.com/repos/' + StarRepoOwnerNames[i] + '/' + \
                                                 StarRepoNames[i] + '/commits?sha=' + dic[
                                                     key] + '&per_page=10'  # 仓库commits情况url
                print(StarRepoBranch_commits_api_url)

        '''
        req3 = requests.get(StarRepo_commits_api_url)
        if req3.status_code != 200:
            print(f'star仓库的分支commits情况请求出错！状态码：{req3.status_code}')
            break
        else:
            req_list3 = req3.json()

            print(f'\nstar的第{i+1}个仓库"{StarRepoNames[i]}"共有如下{len(req_list2)}个分支：\n')

            print(f'第{}个分支"{}"共有如下{len(req_list2)}个分支：\n')

            for j in range(0,len(req_list3)): # 按照时间最近到最早的顺序输出
                print(f'第{j+1}次修改：')
                print('修改者：', req_list3[j]['commit']['author']['name'],
                      '\n修改时间：',req_list3[j]['commit']['author']['date'],
                      '\n修改动作：',req_list3[j]['commit']['message'])
                print('-----------------------------------------------')
        '''