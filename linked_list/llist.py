class LNode:

    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


# 单链表
class LList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    # 从前端插入节点
    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def pop(self):
        if self._head is None:
            raise ValueError('linkedlist no node')
        elem = self._head.elem
        self._head = self._head.next
        return elem

    def append(self, elem):
        node = LNode(elem)
        if self._head is None:
            self._head = node
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = node

    def pop_last(self):
        if self._head is None:
            raise ValueError('linkedlist no node')
        p = self._head
        # 表中只有一个元素
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        # 知道p.next是最后节点
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e


# 有尾节点的单链表
class LListWithRear(LList):

    def __init__(self):
        LList.__init__(self)
        self._rear = None

    def prepend(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    def pop_last(self):
        if self._head is None:
            raise ValueError('linkedlist no node')
        p = self._head
        # 表中只有一个元素
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        # 知道p.next是最后节点
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e