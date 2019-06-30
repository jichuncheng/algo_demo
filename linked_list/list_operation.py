from linked_list.llist import LCList


class ListOperator:

    # 顺序表排序
    @classmethod
    def list_sort(cls, lst):
        for i in range(1, len(lst)):
            x = lst[i]
            j = i
            while j > 0 and lst[j-1] > x:
                lst[j] = lst[j-1]
                j -= 1
            lst[j] = x
        return lst

    # 基于list解决问题
    @staticmethod
    def solution_list(n, k, m):
        """
        # question
        # 假设n个人围坐一圈，从第k个人开始报数，报到第m个数的人退出，然后从下一个人开始继续报数同样规则退出，
        # 直到所有人推出。
        """
        people = list(range(1, n+1))
        i = k - 1
        for num in range(n):
            count = 0
            while count < m:
                if people[i] > 0:
                    count += 1
                if count == m:
                    print(people[i], end="")
                    people[i] = 0
                i = (i+1) % n
            if num < n - 1:
                print(", ", end="")
            else:
                print("")
        return

    # 顺序表的解法
    @staticmethod
    def solution_linked_list(n, k, m):
        people = list(range(1, n+1))

        num, i = n, k-1
        for num in range(n, 0, -1):
            i = (i + m - 1) % num
            print(people.pop(i), end=", " if num > 1 else "\n")
        return


# 基于循环双链表解决该问题
class Solution(LCList):

    def __init__(self):
        LCList.__init__(self)

    def turn(self, m):
        for i in range(m):
            self._rear = self._rear.next

    def sort_(self, n, k, m):
        for i in range(n):
            self.append(i)
        self.turn(k-1)
        while not self.is_empty():
            self.turn(m-1)
            print(self.pop(), end="\n" if self.is_empty() else ", ")


if __name__ == '__main__':
    ListOperator.solution_list(10, 2, 7)
    ListOperator.solution_linked_list(10, 2, 7)
    solu = Solution()
    solu.sort_(10, 2, 7)
