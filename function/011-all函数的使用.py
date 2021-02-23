#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   011-all函数的使用.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/2/23 17:43   muyisanshuiliang      3.9   
@Desciption:
---------------------------------------------------------------     
'''

# import lib

A = [1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8]
# 列表中所有的后一个元素都 >= 前一个元素
result = all([A[i + 1] >= A[i] for i in range(len(A) - 1)])
print(result)

A.reverse()
# 列表中所有的后一个元素都 <= 前一个元素
result = all([A[i + 1] <= A[i] for i in range(len(A) - 1)])
print(result)
