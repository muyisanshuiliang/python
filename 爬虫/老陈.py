import requests
from bs4 import BeautifulSoup

html_url = 'https://www.toutiao.com/c/user/token/MS4wLjABAAAABdvGqHw3p8gwyrCXaHXXydakd1zFcSjsKN4Ns-gtAdA/?tab=article'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
root_url = 'https://www.toutiao.com'


# 主方法
def main():
    res = requests.get(html_url, headers)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, "html.parser")
        items = soup.select(
            "#root > div.profile-container > div.toutiao-header > div.topbar >div.left-nav > ul.nav-list > li.nav-item")
        items.extend(soup.select(
            "#root > div.profile-container > div.toutiao-header > div.topbar >div.left-nav > ul.nav-list > div.nav-layer > ul.nav-more-list > li.nav-more-item"))
        for i, item in enumerate(items):
            if item.a['href'] == '#':
                continue
            print(str(i + 1) + '：' + item.string)
            # print(type(item.a['href']))
            if str(item.a['href']).startswith('//'):
                print("链接地址：https:" + item.a['href'])
            else:
                print("链接地址：" + root_url + item.a['href'])
            print("-" * 50)
    else:
        print("服务器没响应")


if __name__ == '__main__':
    main()
