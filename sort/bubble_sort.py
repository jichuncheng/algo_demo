"""
冒泡排序 冒泡排序只会操作相邻的两个数据。
每次冒泡操作都会对相邻的两个元素进行比较，看是否满足大小关系要求。
如果不满足就让它俩互换。
"""
import copy


def bubble_sort(input_array):
    result_list = copy.deepcopy(input_array)
    length = len(result_list)
    if length <= 1:
        return result_list
    for i in range(length):
        flag = False
        for j in range(length-i-1):
            if result_list[j] > result_list[j+1]:
                result_list[j], result_list[j+1] = result_list[j+1], result_list[j]
                flag = True
        if not flag:
            break
    return result_list


if __name__ == '__main__':
    li = [4,5,6,3,2,1]
    res = bubble_sort(li)
    print(res)