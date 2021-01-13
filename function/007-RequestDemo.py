
import requests
from lxml import html

# 获取源码
page = requests.get("http://www.chenyunkeji.com/")
# 打印源码
tree = html.fromstring(page.text)
# content = tree.xpath('//*[@id="mainBox"]/main/div[2]/div/h4/a/text()')
content = tree.xpath('//html/body/div[1]/div/div[1]/article/header/h2/a/text()')
for each in content:
    replace = each.replace('\n', '').replace(' ', '')
    if replace == '\n' or replace == '':
        continue
    else:
        print(replace)