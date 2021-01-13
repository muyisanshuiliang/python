import os

# 查看当前操作系统的名称。windows平台下返回‘nt’，Linux则返回‘posix’。
print(os.name)

# 获取系统环境变量
x = os.environ
for i in x:
    print("%s == %s " %(i,x.get(i)))