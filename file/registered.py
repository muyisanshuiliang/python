name = input('username>>>: ').strip()
pwd = input('password>>>: ').strip()
with open('db1.txt', mode='a', encoding='utf-8') as f:
    info = '%s:%s\n' % (name, pwd)
    f.write(info)
