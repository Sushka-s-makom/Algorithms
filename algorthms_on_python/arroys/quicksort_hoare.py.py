"""
Algorithm: QuickSort (3-way partition into three lists)

Идея (разделяй и властвуй):
1) Выбираем опорный элемент (pivot, "барьер").
2) Разбиваем массив на три части:
   - L: элементы меньше pivot
   - M: элементы равные pivot
   - R: элементы больше pivot
3) Рекурсивно сортируем L и R.
4) Склеиваем: quicksort(L) + M + quicksort(R)

Асимптотики:
Time complexity:
    Average: O(n log n)
    Worst:   O(n^2)   (например, если pivot всё время минимальный/максимальный)
Space complexity:
    Average: O(n)     (из-за дополнительных списков на каждом уровне)
    Worst:   O(n^2)   (в худшем случае по суммарным выделениям, плюс глубина рекурсии)

Notes:
    - Это не in-place сортировка (создаёт новые списки).
    - Хорошо работает на массивах с большим числом повторов (3-way partition).
"""


def quicksort_three_lists(a):
    if len(a) <= 1:
        return a

    pivot = a[0]
    L, M, R = [], [], []

    for x in a:
        if x < pivot:
            L.append(x)
        elif x == pivot:
            M.append(x)
        else:
            R.append(x)

    return quicksort_three_lists(L) + M + quicksort_three_lists(R)


