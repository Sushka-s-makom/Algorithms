"""
Algorithm: MergeSort (divide and conquer)

Sorts list A using MergeSort:
- split into halves
- recursively sort halves
- merge two sorted halves

Time complexity:
    O(n log n)
Space complexity:
    O(n) extra (for merging) + recursion overhead

Stable:
    Yes (because merge uses <= for equal elements)
"""

from algorithm_merge import merge


def merge_sort(A):
    if len(A) <= 1:
        return A

    middle = len(A) // 2
    L = [A[i] for i in range(0, middle)]
    R = [A[i] for i in range(middle, len(A))]

    L = merge_sort(L)
    R = merge_sort(R)

    return merge(L, R)




