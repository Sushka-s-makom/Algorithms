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



