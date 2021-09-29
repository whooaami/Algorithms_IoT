import unittest
from stack import Node, Stack
from collections import deque


class TestStack(unittest.TestCase):

    def test_push(self):
        test_stack = Stack()
        test_stack.push(4)
        test_stack.push(5)
        test_stack.push(6)
        test_stack.push(7)

        test_stack_list = test_stack.stack_to_list()

        right_stack = deque()
        right_stack.appendleft(4)
        right_stack.appendleft(5)
        right_stack.appendleft(6)
        right_stack.appendleft(7)

        right_stack_list = list(right_stack)

        self.assertEqual(test_stack_list, right_stack_list)

    def test_pop(self):
        test_stack = Stack()
        test_stack.push(4)
        test_stack.push(5)
        test_stack.push(6)
        test_stack.push(7)
        test_stack.pop()

        test_stack_list = test_stack.stack_to_list()

        right_stack = deque()
        right_stack.appendleft(4)
        right_stack.appendleft(5)
        right_stack.appendleft(6)
        right_stack.appendleft(7)
        right_stack.popleft()
        right_stack_list = list(right_stack)

        self.assertEqual(test_stack_list, right_stack_list)

    def test_size(self):
        test_stack = Stack()
        test_stack.push(4)
        test_stack.push(5)
        test_stack.push(6)
        test_stack.push(7)
        test_stack_size = test_stack.size()

        right_stack = deque()
        right_stack.appendleft(4)
        right_stack.appendleft(5)
        right_stack.appendleft(6)
        right_stack.appendleft(7)
        right_stack_size = len(right_stack)

        self.assertEqual(test_stack_size, right_stack_size)
