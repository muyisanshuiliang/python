"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits.__len__() == 0:
            return []
        result = ['']
        number_char_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        for k in digits:
            result = [i + j for i in result for j in number_char_dict[k]]
        print(result)


        result = []
        self.__combine(0, result, digits, number_char_dict, '')
        print(result.__len__())
        return result

    """
    index：递归的起始位置
    result：结果集
    digits：数字串
    number_char_dict：数字串字典
    start_char：起始字符
    """

    def __combine(self, index, result, digits, number_char_dict, start_char):
        # 如果遍历到数字串的末尾，则结束递归，并把元素添加到结果集中
        if index >= len(digits):
            result.append(start_char)
            return
        # 若尚未遍历到数字串的末尾，获取当前位置数字所对应的字符串
        index_ = number_char_dict[digits[index]]
        # 对字符串进行循环处理，对后面的字符串继续进行递归操作
        for item_index, item_val in enumerate(index_):
            self.__combine(index + 1, result, digits, number_char_dict, start_char + item_val)
            # print(result)


print(Solution().letterCombinations("23"))
