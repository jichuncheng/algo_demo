"""
插入排序
将数组中的数据分为两个区间，已排序区间和未排序区间。
初始已排序区间只有一个元素，就是数组的第一个元素。
插入算法的核心思想是取未排序区间中的元素，在已排序区间中找到合适的插入位置将其插入，并保证已排序区间数据一直有序。
重复这个过程，直到未排序区间中元素为空，算法结束。
"""


def insert_sort(input_nums):
    length = len(input_nums)
    for i in range(1, length):
        min = input_nums[i]
        j = i - 1
        while j >= 0:
            if input_nums[j] > min:
                input_nums[j+1] = input_nums[j]
                j -= 1
            else:
                break
        input_nums[j+1] = min


def insert_sort_v2(input_nums):
    length = len(input_nums)
    for i in range(1, length):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i, 0, -1):
            if input_nums[j] < input_nums[j-1]:
                input_nums[j], input_nums[j-1] = input_nums[j-1], input_nums[j]


if __name__ == '__main__':
    li = [4,5,6,3,2,1]
    insert_sort_v2(li)
    print(li)
