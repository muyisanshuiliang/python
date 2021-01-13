import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
url = "https://movie.douban.com/cinema/nowplaying/guangzhou/"


# 主方法
def main():
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, "html.parser")
        print(soup.prettify())
        items = soup.select("#nowplaying > div.mod-bd > ul.lists > li.list-item")


        # 去掉子标签ul
        [s.extract() for s in soup("ul")]
        for i, item in enumerate(items):
            print(str(i + 1)+".", item["data-title"], item["data-release"])
            print("评分:", item["data-score"])
            print(item["data-duration"], item["data-region"])
            print("导演:", item["data-director"])
            print("主演:", item["data-actors"])
            print("-" * 50)
    else:
        print("服务器没响应")


if __name__ == '__main__':
    main()