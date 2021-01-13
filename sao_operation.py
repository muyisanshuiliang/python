# 交叉赋值
m = 10
n = 21
m, n = n, m
print(m, n)

# 解压赋值,字符串、字典、元组、集合类型都支持解压赋值
nums = [11, 22, 33, 44, 55]
# 变量的数量必须与list的个数相等，否则会报错
# a, b = nums
a, b, c, d, e = nums
print(a, b, c, d, e)

# while-else 结构
count = 0
while count <= 5:
    count += 1
    print("Loop", count)
else:
    print("循环正常执行完啦")
print("-----out of while loop ------")

# b: 读写都是以二进制位单位
with open('1.mp4', mode='rb') as f:
    data = f.read()
    print(type(data))  # 输出结果为：<class 'bytes'>

with open('a.txt', mode='wb') as f:
    msg = "你好"
    res = msg.encode('utf-8')  # res为bytes类型
    f.write(res)  # 在b模式下写入文件的只能是bytes类型

# 强调：b模式对比t模式
# 1、在操作纯文本文件方面t模式帮我们省去了编码与解码的环节，b模式则需要手动编码与解码，所以此时t模式更为方便
# 2、针对非文本文件（如图片、视频、音频等）只能使用b模式
