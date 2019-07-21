# 基于顺序表实现的栈
from linked_list.llist import LNode
from stack_and_queue.exceptions import StackUnderflow, QueueUnderflow, PrioQueueError


class SStack:

    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if self._elems == []:
            raise StackUnderflow("stack is None")
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self._elems == []:
            raise StackUnderflow("stack is None")
        return self._elems.pop()


# 基于链接表技术实现的栈
class LStack:

    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise StackUnderflow("stack is None")
        return self._top.elem

    def push(self, elem):
        self._top = LNode(elem, self._top)

    def pop(self):
        if self._top is None:
            raise StackUnderflow("stack is None")
        p = self._top
        self._top = p.next
        return p.elem
