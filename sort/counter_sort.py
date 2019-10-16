# 计数排序


def counter_sort(input_nums):
    n = len(input_nums)
    if n <= 1:
        return

    #  查找数组中数据的范围
    _max = input_nums[0]
    for i in range(1, n):
        if _max < input_nums[i]:
            _max = input_nums[i]

    # 申请一个计数列表
    counter_list = [0] * (_max+1)

    # 计算每个元素的个数,放入 c 中
    for i in range(n):
        counter_list[input_nums[i]] += 1

    # 依次累加
    for i in range(1, _max+1):
        counter_list[i] = counter_list[i-1] + counter_list[i]

    # 计算排序的关键步骤,有点难理解
    tmp = [None] * n
    for i in range(n-1, -1, -1):
        index = counter_list[input_nums[i]] - 1
        tmp[index] = input_nums[i]
        counter_list[input_nums[i]] -= 1

    for i in range(n):
        input_nums[i] = tmp[i]


if __name__ == '__main__':
    li = [2,5,3,0,2,3,0,3]
    counter_sort(li)
    print(li)