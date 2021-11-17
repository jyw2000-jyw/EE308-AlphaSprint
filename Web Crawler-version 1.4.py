import requests
id = 'jyw2000-jyw'
repos_name = 'Bad-movies'

def languageChart():
    lanuage_api_url = 'https://api.github.com/repos/' + id + '/' + repos_name + '/languages' # 仓库语言占比url
    headers={"Authorization":"token "+"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"} # token 增加请求次数
    req4 = requests.get(lanuage_api_url,headers = headers)
    languageDict = req4.json()

    languages = list(languageDict.keys())
    code_quantity = list(languageDict.values())
    
    print(languageDict) # 字典形式：键为语言类型；值为代码量
    
    print(f'\n用户"{id}"的仓库"{repos_name}"使用语言占比如下：\n')

    for i in range(0,len(code_quantity)):
        print(f'{languages[i]}的占比：','{:.2%}'.format(code_quantity[i]/sum(code_quantity)))

    import matplotlib.pyplot as plt  
    data = code_quantity #准备数据
    labels = languages #准备标签

    fig = plt.figure()
    plt.pie(data, labels = labels, autopct='%1.2f%%') #画饼图（数据，数据对应的标签，百分数保留两位小数点）
    plt.title(f'Languages Percentage of \n repository "{repos_name}"')

    plt.show()  
