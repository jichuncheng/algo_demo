# 快速排序


def quick_sort(input_nums, left, right):
    if left < right:
        pivot = partition(input_nums, left, right)
        quick_sort(input_nums, left, pivot-1)
        quick_sort(input_nums, pivot+1, right)


def partition(li, left, right):
    pivot = li[left]
    while left < right:
        while left < right and li[right] >= pivot:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= pivot:
            left += 1
        li[right] = li[left]
    li[left] = pivot
    return left


if __name__ == '__main__':
    li = [4,5,6,3,2,1]
    quick_sort(li, 0, len(li)-1)
    print(li)
