import re

import requests

res = requests.get("https://www.qiushibaike.com/text/")
if res.status_code == 200:
    html = res.text
    # print(html)
    content = re.findall(r'<div class="content">(.*?)</div>', html, re.S)
    sub = re.sub(r"\\n|<br/>", "", str(content))
    print(sub)
    print(re.findall(r'<span>(.*?)</span>', sub, re.S))
    print('================================')
    result = re.sub(r"\\n|<br/>", "",
                    str(re.findall(r'<div class="content">(.*?)</div>', html, re.S)))
    items = re.findall(r'<span>(.*?)</span>', result, re.S)
    for i, text in enumerate(items):
        print(str(i + 1) + ".", text)
else:
    print("服务器没响应")