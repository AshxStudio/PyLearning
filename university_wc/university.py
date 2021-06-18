# import bs4
# from urllib import request
# from bs4 import BeautifulSoup
#
# '''（1）获取网站页面'''
# def getHTMLText(url):
#     try:
#         resp = request.urlopen(url)
#         html_data = resp.read().decode('utf-8')
#         return html_data
#     except:
#         return ""
#
# '''（2）处理页面，提取相关信息'''
# def fillUnivList(ulist, html):
#
#     soup = BeautifulSoup(html, "html.parser")
#     for tr in soup.find('tbody').children:  #搜索'tbody'后面的子节点
#         if isinstance(tr, bs4.element.Tag):
#             tds = tr('td')
#             ulist.append([tds[0].string, tds[1].string, tds[3].string])
#
# '''（3）解析数据，格式化输出结果'''
# def printUnivList(ulist, num):
#     tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
#     print(tplt.format("排名", "学校名称", "总分", chr(12288)))
#     for i in range(num):
#         u = ulist[i]
#         print(tplt.format(u[0], u[1], u[2], chr(12288)))
#
# if __name__ == '__main__':
#     uinfo = []
#     url = ' http://www.shanghairanking.cn/rankings/bcur/202111'
#     html = getHTMLText(url)
#     fillUnivList(uinfo, html)
#     printUnivList(uinfo, 20)    #  输出前20个大学排名　

import requests


def getHTNLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.json()
    except:
        return ""


def fillUnivlist(ulist, dic):
    for ranking in dic['data']['rankings']:
        u = []
        u.append(ranking['ranking'])
        u.append(ranking['univNameCn'])
        u.append(ranking['score'])
        ulist.append(u)


def printUnivlist(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名", "学校名称", "总分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))


def main():
    uinfo = []
    url = 'https://www.shanghairanking.cn/api/pub/v1/bcur?bcur_type=11&year=2021'
    dic = getHTNLText(url)
    fillUnivlist(uinfo, dic)
    printUnivlist(uinfo, 20)


if __name__ == '__main__':
    main()
