#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   XOR.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/2/6 16:18   muyisanshuiliang      3.9   
@Desciption:
---------------------------------------------------------------
（1）一个值与自身的运算，总是为 false：x ^ x = 0
（2）一个值与 0 的运算，总是等于其本身：x ^ 0 = x
（3）可交换性：x ^ y = y ^ x
（4）结合性：x ^ (y ^ z) = (x ^ y) ^ z
'''

# import lib


# 通过异或进行值的交换计算，这是两个变量交换值的最快方法，不需要任何额外的空间。
x = 23
y = 33
x = x ^ y
y = x ^ y
x = x ^ y
print(x, y)

