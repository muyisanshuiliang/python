"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:
输入: num1 = "2", num2 = "3"
输出: "6"

示例 2:
输入: num1 = "123", num2 = "456"
输出: "56088"

说明：
num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # return str(int(num1) * int(num2))
        if num1 == '0' or num2 == '0':
            return '0'

        def __get_num(num_str: str, num_len: int) -> int:
            num = 0
            l = list(num_str)
            l.reverse()
            for item in range(num_len):
                num = num + int(l[item]) * (10 ** item)
            return num

        print(__get_num(num1, len(num1)))
        print(__get_num(num2, len(num2)))
        return str(__get_num(num1, len(num1)) * __get_num(num2, len(num2)))


print(Solution().multiply(num1="123", num2="456"))
