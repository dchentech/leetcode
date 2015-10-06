"""
Question:
    Implement Queue using Stacks

    Implement the following operations of a queue using stacks.

    push(x) -- Push element x to the back of queue.
    pop() -- Removes the element from in front of queue.
    peek() -- Get the front element.
    empty() -- Return whether the queue is empty.

    Notes:
    You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
    Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
    You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

Performance:
    1. Total Accepted: 18785 Total Submissions: 55431 Difficulty: Easy
    2. Your runtime beats 21.35% of python submissions.

Design note:
    At first time, it's hard to think that Queue and Stack are absolutely two different thing.

    How to get the first element in a stack?

    Well, we must use another storage to store the poped items, Yes, add another stack!

    Of course, it's weird. After check discussion of leetcode, it's valid.
"""

class Stack(object):

    def __init__(self):
        self.stack = list()

    def push(self, x):
        return self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def empty(self):
        return self.size() == 0


class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left_stack = Stack()  # master
        self.right_stack = Stack()  # slave

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.left_stack.push(x)

    def pop(self):
        """
        :rtype: nothing
        """
        return self.pop_peek_common(True)

    def peek(self):
        """
        :rtype: int
        """
        return self.pop_peek_common(False)

    def empty(self):
        """
        :rtype: bool
        """
        return self.left_stack.empty()

    def pop_peek_common(self, should_delete):
        while self.left_stack.size() > 0:
            item = self.left_stack.pop()
            self.right_stack.push(item)

        the_item = self.right_stack.pop()
        if not should_delete:
            self.left_stack.push(item)

        while not self.right_stack.empty():
            item = self.right_stack.pop()
            self.left_stack.push(item)

        return the_item

q = Queue()
assert q.empty() is True
q.push(1)
assert q.peek() == 1
assert q.empty() is False
assert q.pop() == 1
assert q.empty() is True
q.push(2)
q.push(3)
q.push(4)
assert q.empty() is False
assert q.peek() == 2
