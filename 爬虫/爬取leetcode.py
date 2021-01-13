import re

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
url = "https://leetcode-cn.com/problemset/all/"

base_url = 'https://leetcode-cn.com'


# 主方法
def main():
    res = requests.get(url, headers)
    if res.status_code == 200:
        re_str = r'<tr>(.*?)<tr>'
        findall = re.findall(re_str, res.text)
        # print(findall)
        soup = BeautifulSoup(res.text, "html.parser")
        # print(soup.prettify())
        select = soup.select('#current-topic-tags > a')
        urls = []
        for i in select:
            # print('=' * 50)
            # print(base_url + i['href'])
            urls.append(base_url + i['href'])
            # print(i.span.string.strip())
        print(urls)
        for item in urls:
            res = requests.get(item, headers)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, "html.parser")
                select = soup.select('#app')
                print(select)
            else:
                pass
    else:
        print("服务器没响应")


if __name__ == '__main__':
    main()
