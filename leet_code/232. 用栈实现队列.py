#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   232. 用栈实现队列.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/3/5 11:14   muYiSanShuiLiang      3.9
@Description:
---------------------------------------------------------------
请你仅使用两个栈实现先入先出队列。队列应当支持一般队列的支持的所有操作（push、pop、peek、empty）：
实现 MyQueue 类：
void push(int x) 将元素 x 推到队列的末尾
int pop() 从队列的开头移除并返回元素
int peek() 返回队列开头的元素
boolean empty() 如果队列为空，返回 true ；否则，返回 false
 
说明：
你只能使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
 
进阶：
你能否实现每个操作均摊时间复杂度为 O(1) 的队列？换句话说，执行 n 个操作的总时间复杂度为 O(n) ，即使其中一个操作可能花费较长时间。

示例：
输入：
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
输出：
[null, null, null, 1, 1, false]
解释：
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
 
提示：
1 <= x <= 9
最多调用 100 次 push、pop、peek 和 empty
假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）
'''


# import lib
class MyQueue:

    # def __init__(self):
    #     """
    #     Initialize your data structure here.
    #     """
    #     self.__stack_input = []
    #     self.__stack_output = []
    #
    # def push(self, x: int) -> None:
    #     """
    #     Push element x to the back of queue.
    #     """
    #     self.__stack_input.append(x)
    #
    # def pop(self) -> int:
    #     """
    #     Removes the element from in front of queue and returns that element.
    #     """
    #     if not self.__stack_output:
    #         while self.__stack_input:
    #             self.__stack_output.append(self.__stack_input.pop())
    #     return self.__stack_output.pop()
    #
    # def peek(self) -> int:
    #     """
    #     Get the front element.
    #     """
    #     if not self.__stack_output:
    #         while self.__stack_input:
    #             self.__stack_output.append(self.__stack_input.pop())
    #     return self.__stack_output[-1]
    #
    # def empty(self) -> bool:
    #     """
    #     Returns whether the queue is empty.
    #     """
    #     return self.__stack_input.__len__() == 0 and self.__stack_output.__len__() == 0

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        self.front = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.s1:
            self.front = x
        self.s1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.s2:
            return self.s2[-1]
        return self.front

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.s1 and not self.s2:
            return True
        return False


queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue)
