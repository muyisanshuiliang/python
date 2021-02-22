#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   行政区划.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/2/1 16:27   muyisanshuiliang      3.9   
@Desciption:
---------------------------------------------------------------     
'''

# import lib
import json

import requests
from bs4 import BeautifulSoup


# 获取省级目录
def getProvince(url):
    data = requests.get(url)
    html = data.content
    html_doc = str(html, 'gbk')
    soup = BeautifulSoup(html_doc, 'html.parser')
    hreflist = soup.findAll('a', href=True)
    provurl = []
    for h in hreflist:
        if '京ICP备' in h.get_text():
            continue
        provurl.append([h.get_text(), h['href']])
    return provurl


# 获取市级目录
def getCity(url):
    data = requests.get(url)
    html = data.content
    html_doc = str(html, 'gbk')
    soup = BeautifulSoup(html_doc, 'html.parser')
    # print(soup)
    trlist = soup.findAll('tr', attrs={'class': 'citytr'})
    citylist = []
    for h in trlist:
        alist = h.findAll('a', href=True)
        citycode = alist[0].get_text()
        cityname = alist[1].get_text()
        cityurl = alist[0]['href']
        citylist.append([citycode, cityname, cityurl])
    return citylist


# 获取区县目录
def getCounty(url):
    data = requests.get(url)
    html = data.content
    html_doc = str(html, 'gb18030', 'ignore')
    soup = BeautifulSoup(html_doc, 'html.parser')
    trlist = soup.findAll('tr', attrs={'class': 'countytr'})
    countylist = []
    for h in trlist:
        alist = h.findAll('a', href=True)
        if len(alist) > 0:
            countycode = alist[0].get_text()
            countyname = alist[1].get_text()
            countyurl = alist[0]['href']
            countyurl = countycode[0:2] + '/' + countyurl
            countylist.append([countycode, countyname, countyurl])
        else:
            attr = h.findAll('td')
            countylist.append([attr[0].get_text(), attr[1].get_text(), 'null'])
    return countylist


# 获取乡镇街道目录
def getTown(url):
    data = requests.get(url)
    html = data.content
    html_doc = str(html, 'gb18030', 'ignore')
    soup = BeautifulSoup(html_doc, 'html.parser')
    trlist = soup.findAll('tr', attrs={'class': 'towntr'})
    townlist = []
    for h in trlist:
        alist = h.findAll('a', href=True)
        if len(alist) > 0:
            towncode = alist[0].get_text()
            townname = alist[1].get_text()
            townurl = alist[0]['href']
            townurl = towncode[0:2] + '/' + towncode[2:4] + '/' + townurl
            townlist.append([towncode, townname, townurl])
        else:
            attr = h.findAll('td')
            townlist.append([attr[0].get_text(), attr[1].get_text(), 'null'])
    return townlist


# 获取村社区目录
def getVillage(url):
    data = requests.get(url)
    html = data.content
    html_doc = str(html, 'gb18030', 'ignore')
    soup = BeautifulSoup(html_doc, 'html.parser')
    trlist = soup.findAll('tr', attrs={'class': 'villagetr'})
    villagelist = []
    for h in trlist:
        attr = h.findAll('td')
        villagelist.append([attr[0].get_text(), attr[1].get_text(), attr[2].get_text()])
    return villagelist


def write_data_to_file(data, file_name):
    try:
        with open(file_name, "w", encoding="utf-8") as f1:
            content = json.dumps(data, ensure_ascii=False)
            f1.write(content)
    except Exception as e:
        raise Exception('Save ERROR:', e)


def read_data_to_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f1:
            data = f1.readline()
            split = data.split(',')
            split_url = []
            for item in split:
                if item.__contains__('html'):
                    split_url.append(item[2:-2])
            return split_url
    except Exception as e:
        raise Exception('Save ERROR:', e)


def get_village_from_file():
    village_url = read_data_to_file("C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\\file\\镇_1.txt")
    village = []
    for item in village_url:
        village.extend(getVillage("http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2020/" + item))
    write_data_to_file(village, "C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\\file\\村_1.txt")
    print("获取村完毕")

    village_dict = {}
    for item in village:
        village_dict[item[0]] = item[2]
    write_data_to_file(village_dict, "C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\\file\\村.txt")
    print("执行完毕")


if __name__ == '__main__':
    url = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2020/"
    # province = getProvince(url)
    # write_data_to_file(province, "C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\\file\\省_1.txt")
    # print("获取省完毕")
    #
    # city = []
    # # province_dict = {}
    # province_str = ''
    # for item in province:
    #     city.extend(getCity("http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2020/" + item[-1]))
    #     # province_dict[item[-1][0:2]] = item[0]
    #     province_str = province_str + str(item[0]) + ':' + str(item[1]) + ';'
    # # write_data_to_file(province, "C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\\file\\省.txt")
    # write_data_to_file(province_str, "C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\\file\\省_str_1.txt")
    # write_data_to_file(city, "C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\\file\\市_1.txt")
    # print("获取市完毕")
    #
    # county = []
    # # city_dict = {}
    # city_str = ''
    # for item in city:
    #     county.extend(getCounty("http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2020/" + item[-1]))
    #     # city_dict[item[0][0:4]] = item[1]
    #     city_str = city_str + str(item[0]) + ':' + str(item[1]) + ':' + str(item[2]) + ';'
    # # write_data_to_file(city, "C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\\file\\市.txt")
    # write_data_to_file(city_str, "C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\\file\\市_str_1.txt")
    # write_data_to_file(county, "C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\\file\\县_1.txt")
    # print("获取县完毕")
    #
    # town = []
    # # county_dict = {}
    # county_str = ''
    # for item in county:
    #     town.extend(getTown("http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2020/" + item[-1]))
    #     # county_dict[item[0][0:6]] = item[1]
    #     city_str = city_str + str(item[0]) + ':' + str(item[1]) + ':' + str(item[2]) + ';'
    # # write_data_to_file(county_dict, "C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\\file\\县.txt")
    # write_data_to_file(city_str, "C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\\file\\县_str_1.txt")
    # write_data_to_file(town, "C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\\file\\镇_1.txt")
    # print("获取镇完毕")

    # village = []
    # town_dict = {}
    # town_str = ''
    # for item in town:
    #     village.extend(getVillage("http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2020/" + item[-1]))
    #     town_dict[item[0][0:9]] = item[1]
    #     town_str = town_str + str(item[0]) + ':' + str(item[1]) + ':' + str(item[2]) + ';'
    # write_data_to_file(town_dict, "C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\\file\\镇.txt")
    # write_data_to_file(town_str, "C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\\file\\镇_str_1.txt")
    # write_data_to_file(village, "C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\\file\\村_1.txt")
    # print("获取村完毕")
    #
    # village_dict = {}
    # village_str = ''
    # for item in village:
    #     village_dict[item[0]] = item[1]
    #     village_str = village_str + str(item[0]) + ':' + str(item[1]) + ':' + str(item[2]) + ';'
    # write_data_to_file(village_str, "C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\\file\\村_str_1.txt")
    # write_data_to_file(village_dict, "C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\\file\\村.txt")
    # print("执行完毕")

    get_village_from_file()
