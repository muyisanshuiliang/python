import requests
from requests.exceptions import RequestException
from lxml import etree
from lxml.etree import ParseError
import xlwings as xw


class LangRanking:
    app = None
    wb = None
    sht = None

    def __init__(self, link):
        self.link = link

    # 创建excel文件
    def open(self):
        self.app = xw.App(visible=True, add_book=False)
        # 新建工作簿
        self.wb = self.app.books.add()
        # 页sheet1
        self.sht = self.wb.sheets["sheet1"]
        # 单元格内容
        self.sht.range("A1").value = "编程语言"
        self.sht.range("B1").value = "排名"

    # 插入数据
    def insert(self, i, lang, order):
        # 按行输入
        self.sht.range("A" + str(i)).value = lang
        self.sht.range("B" + str(i)).value = order

    def create_chart(self):
        chart = self.sht.charts.add(200, 10)
        chart.set_source_data(self.sht.range('A2').expand())
        chart.width = 640
        chart.height = 320
        # 在当前目录下生成文件
        self.wb.save("编程语言琅琊榜.xlsx")
        self.wb.close()
        self.app.quit()

    def get_data(self):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
        }
        try:
            res = requests.get(self.link, headers=headers)
            # 解析HTML文本内容
            html = etree.HTML(res.text, etree.HTMLParser())
            # 定位至需要的标签
            result = html.xpath('// table[ @ id = "top20"] / tbody ')
            self.open()
            index = 2
            for tbody in result:
                tr_list = tbody.xpath('tr')
                for td in tr_list:
                    lang = td[3].text
                    num = td[0].text
                    self.insert(index, lang, num)
                    index += 1
            self.create_chart()
        except RequestException:
            print("请求服务器异常")
        except ParseError:
            print("数据解析错误")


if __name__ == '__main__':
    lr = LangRanking("https://www.tiobe.com/tiobe-index/")
    lr.get_data()