import sys
import requests
from lxml import etree


def get_url(url):  # 请求url的方法，返回html
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    }
    response = requests.get(url, headers=headers)  # 获取请求的返回数据
    response.encoding = 'utf-8'  # 定义编码，不然中文输出会乱码；
    if response.status_code == 200:  # 如果请求成功，则返回；
        return response.text
    return None


data = {}
blue_data = {}
for q in range(1, 125):  # for循环，一共124页；
    url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_%s.html' % (q)  # 定义请求的链接
    html = get_url(url)  # 请求url获取返回代码
    xpath_html = etree.HTML(html)  # xpath初始化html代码

    dates = xpath_html.xpath('//table[@class="wqhgt"]//tr//td[1]//text()')  # 获取开奖日期
    result = xpath_html.xpath('//table[@class="wqhgt"]//tr//em//text()')  # 获取上色球号
    issues = xpath_html.xpath('//table[@class="wqhgt"]//tr//td[2]//text()')  # 获取期号

    sta = 0
    end = 7
    # for n in range(len(result)//7):     #双色球7个号一组，
    #     print("开奖日期:" + str(dates[n]) + " --- " + "期号:" + str(issues[n]) + " --- " + str(result[sta:end]))
    #     sta = sta + 7
    #     end = end + 7

    for n in range(len(result) // 7):  # 双色球7个号一组，
        print("开奖日期:" + str(dates[n]) + " --- " + "期号:" + str(issues[n]) + " --- " + str(result[sta:end]))
        while sta < end:
            if sta % 7 == 6:
                if blue_data.__contains__(result[sta]):
                    value = blue_data.get(result[sta])
                    value = value + 1
                    blue_data[result[sta]] = value
                else:
                    blue_data[result[sta]] = 1
            else:
                if data.__contains__(result[sta]):
                    value = data.get(result[sta])
                    value = value + 1
                    data[result[sta]] = value
                else:
                    data[result[sta]] = 1
            sta = sta + 1
        # sta = sta + 7
        end = end + 7
# data = {'01': 650, '05': 595, '11': 591, '24': 417, '30': 448, '32': 473, '03': 605, '07': 617, '10': 601, '22': 491, '02': 599, '09': 614, '12': 621, '17': 457, '28': 406, '06': 623, '26': 480, '16': 613, '14': 653, '25': 435, '04': 595, '13': 594, '20': 474, '23': 435, '15': 594, '18': 466, '19': 454, '08': 603, '27': 462, '29': 433, '33': 395, '21': 438, '31': 428}
print(sorted(data.items(), key=lambda kv: (kv[1], kv[0])))
print(sorted(blue_data.items(), key=lambda kv: (kv[1], kv[0])))
data = [('33', 395), ('28', 406), ('24', 417), ('31', 428), ('29', 433), ('23', 435), ('25', 435), ('21', 438), ('15', 439), ('11', 440), ('05', 443), ('04', 447), ('12', 447), ('16', 447), ('09', 448), ('30', 448), ('03', 449), ('10', 450), ('02', 452), ('13', 453), ('19', 454), ('07', 457), ('17', 457), ('08', 462), ('27', 462), ('18', 466), ('06', 473), ('32', 473), ('20', 474), ('26', 480), ('01', 487), ('22', 491), ('14', 494)]
blue_data = [('08', 141), ('13', 141), ('02', 147), ('04', 148), ('06', 150), ('10', 151), ('11', 151), ('05', 152), ('15', 155), ('03', 156), ('14', 159), ('07', 160), ('01', 163), ('09', 166), ('16', 166), ('12', 174)]