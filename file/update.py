import os

# 实现思路：以读的方式打开原文件,以写的方式打开一个临时文件,一行行读取原文件内容,修改完后写入临时文件...,删掉原文件,将临时文件重命名原文件名
# 优点: 不会占用过多的内存
# 缺点: 在文件修改过程中同一份数据存了两份
with open('db1.txt', mode='rt', encoding='utf-8') as read_f, \
        open('.db.txt.swap', mode='wt', encoding='utf-8') as wrife_f:
    for line in read_f:
        wrife_f.write(line.replace('zhangsan', 'kevin'))

os.remove('db1.txt')
os.rename('.db.txt.swap', 'db.txt')

# 实现思路：将文件内容发一次性全部读入内存,然后在内存中修改完毕后再覆盖写回原文件
# 优点: 在文件修改过程中同一份数据只有一份
# 缺点: 会过多地占用内存
with open('db.txt', mode='rt', encoding='utf-8') as f:
    data = f.read()

with open('db.txt', mode='wt', encoding='utf-8') as f:
    f.write(data.replace('kevin', 'SB'))
