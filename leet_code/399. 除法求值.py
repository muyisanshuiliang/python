class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        if equations is None or len(equations) == 0:
            return [-1.0] * len(queries)
        equations_dict = {}
        for index in list(range(len(equations))):
            temp = equations[index]
            for item in temp[0]:
                if item in temp[1]:
                    temp[0] = temp[0].strip(item)
                    temp[1] = temp[1].strip(item)
            equations_dict[''.join(temp)] = values[index]
            temp.reverse()
            equations_dict[''.join(temp)] = 1 / values[index]
        return equations_dict


# equations = [["a", "b"], ["b", "c"]]
# values = [2.0, 3.0]
equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
values = [1.5, 2.5, 5.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
solution = Solution()
print(solution.calcEquation(equations, values, queries))
