# for task number 7
# recursive binary search means to subdivide the entire binary search process into smaller problem
import random


def rec_Search(target, sequence, first, last):
    if first > last:
        return False
    else:
        mid = (last + first) // 2
        if sequence[mid] == target:
            return True
        elif target < sequence[mid]:
            return rec_Search(target, sequence, first, mid - 1)
        else:
            return rec_Search(target, sequence, mid + 1, last)


seq = 1, 2, 3, 4, 5, 7, 12, 16, 23, 44, 50
