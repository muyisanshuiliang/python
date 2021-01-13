from bs4 import BeautifulSoup
import requests
url = 'http://shicimingju.com/book/sanguoyanyi.html'
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
fp=open('./fiction.txt','w',encoding='utf-8')
page_text = requests.get(url, headers=headers).text
soup = BeautifulSoup(page_text, 'lxml')
a_list = soup.select('.book-mulu a')
for a in a_list:
    title=a.text
    detail_url='http://shicimingju.com'+a['href']
    detail_text=requests.get(detail_url,headers=headers).text
    soup=BeautifulSoup(detail_text,'lxml')
    content=soup.find('div',class_='chapter_content').text
    fp.write(a.string+':'+content+'\n')
    print(a.string+':\t'+' 爬取成功')
print('全部完成')
