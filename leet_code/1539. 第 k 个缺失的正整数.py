arr = [2, 3, 4, 7, 11]
k = 10
arr_temp = list(range(1, max(arr) + 1))
print(arr_temp)
index = 0
result = 1
while True:
    # 越界，遍历完毕，退出循环
    if index >= len(arr):
        break
    # 如果值与下标相等，指针后移
    if arr[index] == result:
        index += 1
        result += 1
        continue
    else:
        k -= 1
        if k == 0:
            print(result)
            break
        result += 1
print(result + k - 1)
