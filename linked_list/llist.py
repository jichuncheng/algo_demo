class LNode:

    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


# 双链表结点类
class DLNode(LNode):

    def __init__(self, elem, prev=None, next_=None):
        LNode.__init__(elem, next_)
        self.prev = prev


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

    # 调换表元素
    def _sort(self):
        if self._head is None:
            return
        crt = self._head.next
        while crt is not None:
            x = crt.elem
            p = self._head
            while p is not crt and p.elem <= x:
                p = p.next
            while p is not crt:
                y = p.elem
                p.elem = x
                x = y
                p = p.next
            crt.elem = x
            crt = crt.next

    # 修改表链接
    def _sort2(self):
        p = self._head
        if p is None or p.next is None:
            return

        rem = p.next
        p.next = None
        while rem is not None:
            p = self._head
            q = None
            while p is not None and p.elem <= rem.elem:
                q = p
                p = p.next
            if q is None:
                self._head = rem
            else:
                q.next = rem
            q = rem
            rem = rem.next
            q.next = p


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


# 循环单链表
class LCList:

    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    # 前端插入
    def prepend(self, elem):
        p = LNode(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next

    # 首端弹出
    def pop(self):
        if self._rear is None:
            raise ValueError('linkedlist no node')
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem

    def print_all(self):
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p = p.next


# 双链表类
class DLList(LListWithRear):

    def __init__(self):
        LListWithRear.__init__(self)

    def prepend(self, elem):
        p = DLNode(elem, None, self._head)
        if self._head is None:
            self._rear = p
        else:
            p.next.prev = p
        self._head = p

    def append(self, elem):
        p = DLNode(elem, self._rear, None)
        if self._head is None:
            self._head = p
        else:
            p.prev.next = p
        self._rear = p

    def pop(self):
        if self._head is None:
            raise ValueError('linkedlist no node')
        e = self._head.elem
        self._head = self._head.next
        # head为空时什么也不用做
        if self._head is not None:
            self._head.prev = None
        return e

    def pop_last(self):
        if self._head is None:
            raise ValueError('linkedlist no node')
        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is None:
            # 设置 _head保证is_empty正确工作
            self._head = None
        else:
            self._rear.next = None
        return e
