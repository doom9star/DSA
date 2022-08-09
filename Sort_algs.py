def insertion_sort(lst):
    for index in range(1, len(lst)):
        another_ind = index
        while another_ind >= 1:
            if lst[another_ind] < lst[another_ind - 1]:
                lst[another_ind - 1], lst[another_ind] = lst[another_ind], lst[another_ind - 1]
            another_ind -= 1
    print(lst)


def selection_sort(lst):
    for index in range(len(lst)):
        min_val = index
        for another_index in range(index + 1, len(lst)):
            if lst[another_index] <= lst[min_val]:
                min_val = another_index
        if min_val != index:
            lst[index], lst[min_val] = lst[min_val], lst[index]
    print(lst)


def bubble_sort(lst):
    for index in range(len(lst)):
        for another_ind in range(len(lst) - index - 1):
            if lst[another_ind] >= lst[another_ind + 1]:
                lst[another_ind], lst[another_ind + 1] = lst[another_ind + 1], lst[another_ind]
    print(lst)


def merge_sort(lst):
    merge_sort2(lst, 0, len(lst) - 1)
    print(lst)


def merge_sort2(lst, start, end):
    if start < end:
        middle = (start + end) // 2
        merge_sort2(lst, start, middle)
        merge_sort2(lst, middle + 1, end)
        merge(lst, start, middle, end)


def merge(lst, start, middle, end):
    leftside = lst[start:middle]
    rightside = lst[middle:end + 1]
    leftside.append(999999)
    rightside.append(999999)
    i = j = 0
    for index in range(start, end + 1):
        if leftside[i] <= rightside[j]:
            lst[index] = leftside[i]
            i += 1
        else:
            lst[index] = rightside[j]
            j += 1


merge_sort([10, 5, 2, 45, 32, 90, 9, 78, 42, 65, 12, 10, 5, 2, 67, 11, 34, 22, 56,32,11,23])
