"""
Question:

    Implement Stack using Queues

    Implement the following operations of a stack using queues.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    empty() -- Return whether the stack is empty.

    Notes:
    You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
    Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
    You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
    Update (2015-06-11):
    The class name of the Java function had been updated to MyStack instead of Stack.

    Credits:
    Special thanks to @jianchao.li.fighter for adding this problem and all test cases.


Performance:
    1. Total Accepted: 19217 Total Submissions: 63106 Difficulty: Easy

Annotation:
    1. refer to 232-implement-queue-using-stacks.py
    2. Your runtime beats 99.44% of python submissions.
"""


class Queue(object):
    def __init__(self):
        self.queue = list()

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        if self.empty():
            return None
        first_item = self.queue[0]
        self.queue = self.queue[1:]
        return first_item

    def peek(self):
        if self.queue:
            return self.queue[0]
        return None

    def empty(self):
        return not self.queue

    def __repr__(self):
        return str(self.queue)


class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.master_queue = Queue()
        self.slave_queue = Queue()

    def __repr__(self):
        return "<Stack {}>".format(self.master_queue)

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.master_queue.push(x)

    def pop(self):
        """
        :rtype: nothing
        """
        return self.common_pop_top(False)

    def top(self):
        """
        :rtype: int
        """
        return self.common_pop_top(True)

    def common_pop_top(self, keep):
        top_item = None
        while not self.master_queue.empty():  # loop over the master_queue
            item = self.master_queue.pop()
            if self.master_queue.empty():
                top_item = item  # select the last one in the queue
            if keep or (top_item != item):
                self.slave_queue.push(item)
        self.master_queue, self.slave_queue = self.slave_queue, self.master_queue
        return top_item

    def empty(self):
        """
        :rtype: bool
        """
        return self.master_queue.empty()


s = Stack()
assert s.empty() is True
s.push(1)
assert s.top() == 1
assert s.empty() is False
assert s.pop() == 1
assert s.empty() is True
s.push(2)
s.push(3)
s.push(4)
assert s.empty() is False
v = s.top()
assert v == 4, v
assert s.pop() == 4
assert s.pop() == 3
assert s.pop() == 2
assert s.empty() is True
