"""
Algorithms: O(n^2) sorting algorithms (in-place)

Included:
- Insertion sort
- Selection sort
- Bubble sort

Time complexity:
    Insertion sort: average/worst O(n^2), best O(n) on nearly sorted data
    Selection sort: O(n^2) always
    Bubble sort:    average/worst O(n^2), best O(n) with early-exit optimization (not used here)

Space complexity:
    O(1) extra (in-place)
"""

def insert_sort(A):
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k - 1] > A[k]:
            A[k], A[k - 1] = A[k - 1], A[k]
            k -= 1


def choise_sort(A):
    N = len(A)
    for pos in range(0, N - 1):
        for k in range(pos + 1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]


def bubble_sort(A):
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N - bypass):
            if A[k] > A[k + 1]:
                A[k], A[k + 1] = A[k + 1], A[k]


def test_sort(sort_algorithm):
    print("test_case #1:", end=" ")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else f"Fail (got {A})")

if __name__ == "__main__":
    # Run the same test for each algorithm
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(bubble_sort)

