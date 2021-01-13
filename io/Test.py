login_user = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu', 'yangqi']
login_pass_word = ['zs123456', 'ls123456', 'ww123456', 'zl123456', 'yq123456']

count = 5
while count > 0:
    user_name = input("请输入你的用户名：").strip()
    if len(user_name) == 0:
        print("用户名不能为空")
        continue

    count -= 1
    pass_word = input("请输入你的登陆密码：").strip()
    if login_user.__contains__(user_name):
        index = 0
        while user_name != login_user[index]:
            index += 1
        if pass_word != login_pass_word[index]:
            print("你还可以尝试 %d 次" % count)
            print("密码不正确")
        else:
            print("%s 欢迎你的到来！" % user_name)
            break
    else:
        print("%s 用户名不存在。" % user_name)
        print("你还可以尝试 %d 次" % count)
        continue
