from algorithm_merge import merge
def merge_sort (A) :
    if len(A) <= 1 :
        return A
    middle = len(A)//2
    L = [A[i] for i in range (0, middle)]
    R =[A[i] for i in range(middle, len(A))]
    merge_sort(L)
    merge_sort(R)
    return merge(L, R)
