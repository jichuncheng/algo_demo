# 归并排序


def merge_sort(input_list):
    _merge_sort(input_list, 0, len(input_list)-1)


def _merge_sort(input_list, low, high):
    if low < high:
        mid = low + (high - low) // 2
        _merge_sort(input_list, low, mid)
        _merge_sort(input_list, mid + 1, high)
        _merge(input_list, low, mid, high)


def _merge(input_list, low, mid, high):
    i, j = low, mid + 1
    tmp = []
    while i <= mid and j <= high:
        if input_list[i] <= input_list[j]:
            tmp.append(input_list[i])
            i += 1
        else:
            tmp.append(input_list[j])
            j += 1
    start = i if i <= mid else j
    end = mid if i <= mid else high
    tmp.extend(input_list[start:end+1])
    input_list[low:high+1] = tmp


if __name__ == '__main__':
    li = [4,5,6,3,2,1]
    merge_sort(li)
    print(li)