#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   file_cast.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/2/6 15:36   muyisanshuiliang      3.9   
@Desciption:
---------------------------------------------------------------     
'''

# import lib
import json
from typing import List


class FileTrance:

    def get_province_code(self):
        try:
            with open('C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\省.txt', "r", encoding="utf-8") as f1:
                read = f1.read()
                loads = json.loads(read)
                return list(loads.keys())
        except Exception as e:
            raise Exception('Save ERROR:', e)

    def write_city(self, province_code: List[str]):
        try:
            with open('C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\市.txt', "r", encoding="utf-8") as f1:
                city_data = json.loads(f1.read())
        except Exception as e:
            raise Exception('Save ERROR:', e)
        city_code = []
        for item in province_code:
            one_city_data = {}
            for city_key, city_val in city_data.items():
                if city_key.startswith(item):
                    one_city_data[city_key] = city_val
                    city_code.append(city_key)
            try:
                with open('C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\\data_location\\' + item + '.json', "w",
                          encoding="utf-8") as f1:
                    content = json.dumps(one_city_data, ensure_ascii=False)
                    f1.write(content)
            except Exception as e:
                raise Exception('Save ERROR:', e)
        print("市文件写完毕")
        return city_code

    def write_county(self, city_code: List[str]):
        try:
            with open('C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\县.txt', "r", encoding="utf-8") as f1:
                city_data = json.loads(f1.read())
        except Exception as e:
            raise Exception('Save ERROR:', e)
        county_code = []
        for item in city_code:
            one_county_data = {}
            for county_key, county_val in city_data.items():
                if county_key.startswith(item):
                    one_county_data[county_key] = county_val
                    county_code.append(county_key)
            try:
                with open('C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\\data_location\\' + item + '.json', "w",
                          encoding="utf-8") as f1:
                    content = json.dumps(one_county_data, ensure_ascii=False)
                    f1.write(content)
            except Exception as e:
                raise Exception('Save ERROR:', e)
        print("县文件写完毕")
        return county_code

    def write_township(self, county_code: List[str]):
        try:
            with open('C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\镇.txt', "r", encoding="utf-8") as f1:
                township_data = json.loads(f1.read())
        except Exception as e:
            raise Exception('Save ERROR:', e)
        township_code = []
        for item in county_code:
            one_township_data = {}
            for township_key, township_val in township_data.items():
                if township_key.startswith(item):
                    one_township_data[township_key] = township_val
                    township_code.append(township_key)
            try:
                with open('C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\\data_location\\' + item + '.json', "w",
                          encoding="utf-8") as f1:
                    content = json.dumps(one_township_data, ensure_ascii=False)
                    f1.write(content)
            except Exception as e:
                raise Exception('Save ERROR:', e)
        print("乡镇文件写完毕")
        return township_code

    def write_village(self, township_code: List[str]):
        try:
            with open('C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\村.txt', "r", encoding="utf-8") as f1:
                village_data = json.loads(f1.read())
        except Exception as e:
            raise Exception('Save ERROR:', e)
        for item in township_code:
            one_village_data = {}
            for village_key, village_val in village_data.items():
                if village_key.startswith(item):
                    one_village_data[village_key] = village_val
            try:
                with open('C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\\data_location\\' + item + '.json', "w",
                          encoding="utf-8") as f1:
                    content = json.dumps(one_village_data, ensure_ascii=False)
                    f1.write(content)
            except Exception as e:
                raise Exception('Save ERROR:', e)
        print("村文件写完毕")


if __name__ == '__main__':
    trance = FileTrance()
    # print(trance.get_province_code())
    city_code = trance.write_city(trance.get_province_code())
    # print(city_code)
    county_code = trance.write_county(city_code)
    city_code = None
    township_code = trance.write_township(county_code)
    county_code = None
    trance.write_village(township_code)
