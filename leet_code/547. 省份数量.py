EXTEND = [1].extend([])


class Solution(object):
    # def findCircleNum(self, isConnected):
    #     """
    #     :type isConnected: List[List[int]]
    #     :rtype: int
    #     """
    #     if isConnected is None or len(isConnected) == 0:
    #         return 0
    #     length = len(isConnected)
    #     neighbor = []
    #     for i in list(range(length)):
    #         first_neighbor = self.__get_first_neighbor(isConnected=isConnected, index=i, length=length)
    #         neighbor.append(first_neighbor)
    #     print(neighbor)
    #     result = []
    #     for index in list(range(0, len(neighbor))):
    #         print('==============index = %d=====================' % (index))
    #         print(neighbor)
    #         if len(neighbor[index]) == 0:
    #             continue
    #         temp = neighbor[index]
    #         neighbor[index] = []
    #         inner_index = index + 1
    #         while inner_index < length:
    #             if len(neighbor[inner_index]) == 0:
    #                 pass
    #             elif len(set(temp) & set(neighbor[inner_index])) != 0:
    #                 temp = set(temp) | set(neighbor[inner_index])
    #                 neighbor[inner_index] = []
    #             inner_index += 1
    #         for inner_index in list(range(len(result))):
    #             if len(set(result[inner_index]) & set(temp)) != 0:
    #                 result[inner_index] = set(result[inner_index]) | set(temp)
    #                 temp = []
    #                 break
    #         print(temp)
    #         print(neighbor)
    #         if len(temp) != 0:
    #             result.append(set(temp))
    #         print(result)
    #     return len(result)
    #
    # def __get_first_neighbor(self, isConnected, index, length):
    #     j = 0
    #     first_neighbor = set()
    #     while j < length:
    #         if isConnected[index][j] == 1:
    #             first_neighbor.add(j)
    #         j += 1
    #     return first_neighbor

    def find(self, p, x):
        if p[x] != x:
            p[x] = self.find(p, p[x])
        return p[x]

    def merge(self, p, a, b):
        p[self.find(p, a)] = self.find(p, b)

    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        p = [i for i in range(n + 1)]
        print(p)
        for i in range(n):
            for j in range(i, n):
                if isConnected[i][j] == 1:
                    self.merge(p, i + 1, j + 1)
        res = set()
        for i in range(1, n + 1):
            res.add(self.find(p, i))
        return len(res)

    def dfs(self, isConnected):
        neighbor = []
        count = 0
        is_visited = [False] * len(isConnected)
        for item_inx in list(range(len(isConnected))):
            if not is_visited[item_inx]:
                count += 1
                neighbor.append(item_inx)
            while len(neighbor) != 0:
                pop = neighbor.pop()
                # 如果该节点已经进行了查找，则不再进行临接节点的获取
                if is_visited[pop]:
                    continue
                else:
                    # city.append(pop)
                    is_visited[pop] = True
                # 邻接节点压入栈
                neighbor.extend(self.__get_first_neighbor(isConnected, pop))
                # print(city)
        return count

    def bfs(self, isConnected):
        neighbor = []
        # outer_city = list()
        count = 0
        is_visited = [False] * len(isConnected)
        for item_inx in list(range(len(isConnected))):
            if not is_visited[item_inx]:
                count += 1
                neighbor.append(item_inx)
            city = []
            while len(neighbor) != 0:
                pop = neighbor.pop(0)
                # 如果该节点已经进行了查找，则不再进行临接节点的获取
                # if city.__contains__(pop):
                if is_visited[pop]:
                    continue
                else:
                    city.append(pop)
                    is_visited[pop] = True
                # 邻接节点压入栈
                neighbor.extend(self.__get_first_neighbor_head(isConnected, pop))
                # print(city)
                # print(is_visited)
            # if len(city) != 0:
            #     outer_city.append(city)
            # print(outer_city)

        # return len(outer_city)
        return count

    def __get_first_neighbor(self, isConnected, index):
        j = len(isConnected) - 1
        first_neighbor = []
        while j >= 0:
            if isConnected[index][j] == 1 and j != index:
                first_neighbor.append(j)
            j -= 1
        return first_neighbor

    def __get_first_neighbor_head(self, isConnected, index):
        first_neighbor = []
        for item in list(range(len(isConnected))):
            if isConnected[index][item] == 1 and item != index:
                first_neighbor.append(item)
        return first_neighbor


isConnected = [
    # 1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
    [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 1
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3
    [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],  # 5
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # 6
    [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],  # 7
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # 8
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0],  # 9
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],  # 10
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0],  # 11
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],  # 12
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # 13
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],  # 14
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]  # 15
]

def dfs(isConnected):
    # 获取当前节点的邻居节点
    def _get_first_neighbor(isConnected, cur_point):
        j = len(isConnected) - 1
        neighbor = []
        while j >= 0:
            if isConnected[cur_point][j] == 1 and cur_point != j:
                neighbor.append(j)
            j -= 1
        return neighbor

    result = ''
    # 存储邻居节点
    neighbor_stack = []
    # 存储节点的访问状态，默认都是未被访问状态
    is_visited = [False] * len(isConnected)
    for cur_point in range(len(isConnected)):
        # 如果当前节点已经被访问，则对下一个节点进行访问
        if is_visited[cur_point]:
            continue
        # 当前节点置为已被访问状态
        is_visited[cur_point] = True
        result = result + str(cur_point) + '------>'
        # 当前节点的所有邻居节点压入栈中
        neighbor_stack.extend(_get_first_neighbor(isConnected, cur_point))
        # 如果邻居节点为空，说明当前已经是最后的一个节点，否则依次对灵雎节点进行处理
        while neighbor_stack.__len__() != 0:
            # 获取邻居节点
            pop = neighbor_stack.pop()
            # 如果邻居节点已经被访问，则继续处理下一个邻居节点
            if is_visited[pop]:
                continue
            else:
                # 对邻居节点进行遍历
                result = result + str(pop) + '------>'
                # 修改邻居节点的访问状态为已访问
                is_visited[pop] = True
                # 获取邻居节点的邻居节点
                neighbor_stack.extend(_get_first_neighbor(isConnected, pop))
    return result

def bfs(isConnected):
    # 获取当前节点的邻居节点
    def _get_first_neighbor(isConnected, cur_point):
        j = 0
        neighbor = []
        while j < len(isConnected):
            if isConnected[cur_point][j] == 1 and cur_point != j:
                neighbor.append(j)
            j += 1
        return neighbor

    result = ''
    # 存储邻居节点
    neighbor_stack = []
    # 存储节点的访问状态，默认都是未被访问状态
    is_visited = [False] * len(isConnected)
    for cur_point in range(len(isConnected)):
        # 如果当前节点已经被访问，则对下一个节点进行访问
        if is_visited[cur_point]:
            continue
        # 当前节点置为已被访问状态
        is_visited[cur_point] = True
        result = result + str(cur_point) + '------>'
        # 当前节点的所有邻居节点压入栈中
        neighbor_stack.extend(_get_first_neighbor(isConnected, cur_point))
        # 如果邻居节点为空，说明当前已经是最后的一个节点，否则依次对灵雎节点进行处理
        while neighbor_stack.__len__() != 0:
            # 获取邻居节点
            pop = neighbor_stack.pop(0)
            # 如果邻居节点已经被访问，则继续处理下一个邻居节点
            if is_visited[pop]:
                continue
            else:
                # 对邻居节点进行遍历
                result = result + str(pop) + '------>'
                # 修改邻居节点的访问状态为已访问
                is_visited[pop] = True
                # 获取邻居节点的邻居节点
                neighbor_stack.extend(_get_first_neighbor(isConnected, pop))
    return result
# isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# solution = Solution()
# print(solution.findCircleNum(isConnected))
# print(solution.dfs(isConnected))


print("dfs结果：" + dfs(isConnected))
print("dfs结果：" + bfs(isConnected))
