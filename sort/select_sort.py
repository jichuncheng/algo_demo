# 选择排序


def select_sort(input_num):

    length = len(input_num)
    min = 0
    for i in range(length-1):
        for j in range(i+1, length):
            if input_num[j] < input_num[i]:
                input_num[j], input_num[i] = input_num[i], input_num[j]


if __name__ == '__main__':
    li = [4,5,6,3,2,1]
    select_sort(li)
    print(li)