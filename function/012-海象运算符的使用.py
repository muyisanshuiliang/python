#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   012-海象运算符的使用.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/5 15:30   muyisanshuiliang      3.9   
@Description:
---------------------------------------------------------------     
'''

# import lib

a = [1, 2, 3, 4, 5]
# 在这个例子里面，文档强调通过使用海象表达式，避免len()方法运行两次，从而提高了运行速度.
if (n := len(a)) <= 10:
    print(f"List is too long ({n} elements, expected >= 10)")

# 假如在没有海象运算符的时候，我们会怎么来写这段代码呢？来试一试：
if len(a) <= 10:
    print(f"List is to long({len(a)} elements, expected >= 10)")
# 或者这样写，避免使用两次len方法，却又多了一次赋值给中间变量的步骤.
n = len(a)
if n <= 10:
    print(f"List is to long({n} elements, expected >= 10)")

N = [y for item in a if (y := item) % 2 == 0]
print(N)