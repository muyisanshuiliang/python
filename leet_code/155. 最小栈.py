class MinStack(object):

    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.__data = []
    #     self.__min = None
    #
    # def push(self, x):
    #     """
    #     :type x: int
    #     :rtype: None
    #     """
    #     if not self.__data:
    #         self.__data.append(0)
    #         self.__min = x
    #     else:
    #         self.__data.append(x - self.__min)
    #         if x < self.__min:
    #             self.__min = x
    #
    # def pop(self):
    #     """
    #     :rtype: None
    #     """
    #     x = self.__data.pop()
    #     if x < 0:
    #         self.__min = self.__min - x
    #
    # def top(self):
    #     """
    #     :rtype: int
    #     """
    #     x = self.__data[-1]
    #     if x > 0:
    #         return x + self.__min
    #     else:
    #         return self.__min
    #
    # def getMin(self):
    #     """
    #     :rtype: int
    #     """
    #     return self.__min

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__data = []
        self.__min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.__data.append(x)
        if len(self.__min_stack) == 0:
            self.__min_stack.append(x)
        else:
            if self.__min_stack[-1] > x:
                self.__min_stack.append(x)
            else:
                self.__min_stack.append(self.__min_stack[-1])

    def pop(self):
        """
        :rtype: None
        """
        self.__data.pop()
        self.__min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.__data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.__min_stack[-1]
