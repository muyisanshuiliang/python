# 打印金字塔

print(isinstance('-',int))
count = 0
while 1 == 1:
    count = input("请输入你要打印的金字塔层数(奇数)：").strip()
    if count.__len__() == 0:
        print("请输入一个数字")
    elif count == "q":
        print("欢迎下次再来玩耍")
    elif not count.isdigit():
        print("请输入一个整数")
    elif int(count) % 2 == 0:
        print("请输入一个奇数")
    else:
        temp = int(count) // 2
        for current_level in range(1, temp + 1):
            for i in range(temp - current_level):
                print(' ', end='')  # 在一行中连续打印多个空格
            for j in range(2 * current_level - 1):
                print('*', end='')  # 在一行中连续打印多个空格
            print()


