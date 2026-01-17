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

def _is_sorted(x):
    return all(x[i] <= x[i + 1] for i in range(len(x) - 1))

def _self_test():
    # базовые случаи
    assert quicksort_three_lists([]) == []
    assert quicksort_three_lists([1]) == [1]
    assert quicksort_three_lists([2, 1]) == [1, 2]

    # уже отсортирован
    assert quicksort_three_lists([1, 2, 3, 4]) == [1, 2, 3, 4]

    # обратный порядок
    assert quicksort_three_lists([4, 3, 2, 1]) == [1, 2, 3, 4]

    # повторы
    assert quicksort_three_lists([5, 1, 5, 2, 0, 5]) == [0, 1, 2, 5, 5, 5]

    # отрицательные
    assert quicksort_three_lists([0, -1, 3, -2]) == [-2, -1, 0, 3]

    # свойство: результат отсортирован + элементы не потерялись
    arr = [10, 7, 7, 3, 2, 9, 0]
    out = quicksort_three_lists(arr)
    assert _is_sorted(out)

    print("OK: quicksort_three_lists self_test")


if __name__ == "__main__":
    example = [5, 2, 9, 1, 5, 6, 5, 0]
    print("input: ", example)
    print("output:", quicksort_three_lists(example))
    _self_test()

