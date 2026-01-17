"""
Algorithm: Merge two sorted arrays (two pointers)

Merges two lists A and B sorted in non-decreasing order into a new sorted list.

Time complexity:
    O(n + m), where n = len(A), m = len(B)
Space complexity:
    O(n + m) for the output array

Precondition:
    A and B are already sorted.
"""

def merge(A, B):
    C = [0] * (len(A) + len(B))
    i = k = n = 0

    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]; i += 1; n += 1
        else:
            C[n] = B[k]; k += 1; n += 1

    while i < len(A):
        C[n] = A[i]; i += 1; n += 1

    while k < len(B):
        C[n] = B[k]; k += 1; n += 1

    return C


def _is_sorted(x):
    return all(x[i] <= x[i + 1] for i in range(len(x) - 1))


def _self_test():
    # empty cases
    assert merge([], []) == []
    assert merge([1, 2, 3], []) == [1, 2, 3]
    assert merge([], [1, 2]) == [1, 2]

    # interleaving
    assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

    # duplicates
    assert merge([1, 2, 2], [2, 2, 3]) == [1, 2, 2, 2, 2, 3]

    # output sorted
    out = merge([0, 10, 10], [1, 2, 9, 11])
    assert _is_sorted(out)

    print("OK: algorithm_merge self_test")


if __name__ == "__main__":
    print(merge([1, 4, 7], [2, 2, 8]))
    _self_test()
