# res = yield 返回值


def eat(name, ):
    food_list = []
    i = 0
    while i < 2:
        # send 是给 yield 赋值，res = yield 接收到的值
        # 1、将send的值接收，赋给res,
        # 2、执行代码，下次yield，将值返回
        res = yield food_list
        print("%s 吃了 %s ====================> " % (name, res))
        food_list.append(res)
        i += 1


# 有yield 存在就会产生迭代器
generator = eat("十一")
print(generator)

# 每执行一次会得到 yield 后的值，第一次执行会停留在 yield 处
# res = next(generator)
# print(res)

# 等价于 send(None)，初始化
res = next(generator)
print(res)

# 等价于 next(generator)
send = generator.send("一块肉")
print(send)
send = generator.send("一根骨头")
print(send)
send = generator.send("一个包子")
print(send)
