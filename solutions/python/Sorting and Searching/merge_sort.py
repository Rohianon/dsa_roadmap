from typing import List, Optional
from merge import merge

def merge_sort(arr: List[int]) -> Optional[callable]:
    if len(arr) == 1: return arr
    # print(arr)

    mid_point = len(arr)//2
    # print(mid_point)

    # print('h1', arr[:mid_point])
    # print('h2', arr[mid_point:])

    left_half = merge_sort(arr[:mid_point])
    right_half = merge_sort(arr[mid_point:])

    return merge(left_half, right_half)



if __name__ == "__main__":
    arr = [8, 40, 6, 4, 11, 5, 7]
    actual = [4, 5, 6, 7, 8, 11, 40]
    print(merge_sort(arr))
    # assert(arr == actual)