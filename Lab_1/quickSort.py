import time
from enum import Enum


class SortOrder(Enum):
    ASC = 0
    DESC = 1


count = 0
swaps = 0


def quick_sort(array, start, end, type_of_sorting):
    if len(array) <= 1:
        return array

    global count, swaps
    new_pivot = start - 1
    pivot = array[end]

    for elem_to_compare_pos in range(start, end):
        count += 1
        if type_of_sorting == SortOrder.ASC:
            if array[elem_to_compare_pos] <= pivot:
                new_pivot += 1
                swaps += 1
                array[new_pivot], array[elem_to_compare_pos] = array[elem_to_compare_pos], array[new_pivot]
        elif type_of_sorting == SortOrder.DESC:
            if array[elem_to_compare_pos] >= pivot:
                new_pivot += 1
                swaps += 1
                array[new_pivot], array[elem_to_compare_pos] = array[elem_to_compare_pos], array[new_pivot]
    array[new_pivot + 1], array[end] = array[end], array[new_pivot + 1]
    return new_pivot + 1


def partition(array, type_of_sorting, start_pos=0, end_pos=None):
    if end_pos == None:
        end_pos = len(array) - 1
    if start_pos < end_pos:
        pivot_pos = quick_sort(array, start_pos, end_pos, type_of_sorting)
        partition(array, type_of_sorting, start_pos, pivot_pos - 1)
        partition(array, type_of_sorting, pivot_pos + 1, end_pos)


if __name__ == '__main__':
    print('Enter type of sorting: ')
    TypeOfSorting = input()

    if TypeOfSorting == "asc":
        TypeOfSorting = SortOrder.ASC
    else:
        TypeOfSorting = SortOrder.DESC

    new_array = [7, -10, 25, 2, 0, 1, 4]
    result = new_array

    start = time.time()
    partition(result, TypeOfSorting)
    end = time.time()
    execution_time = (end - start) * 1000

    print(f"QuickSort sorted:\n"
          f"Execution time: {execution_time}ms\n"
          f"Comparisons: {count}\n"
          f"Swaps: {swaps}\n"
          f"Result: {result}\n")
