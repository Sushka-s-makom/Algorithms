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


def _is_sorted(x):
    return all(x[i] <= x[i + 1] for i in range(len(x) - 1))


def _self_test():
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    assert merge_sort([2, 1]) == [1, 2]
    assert merge_sort([3, 2, 1]) == [1, 2, 3]
    assert merge_sort([5, 1, 5, 2, 0]) == [0, 1, 2, 5, 5]

    out = merge_sort([10, -1, 2, 2, 9, 0])
    assert _is_sorted(out)

    print("OK: merge_sort self_test")


if __name__ == "__main__":
    print(merge_sort([5, 2, 9, 1, 5, 6]))
    _self_test()

