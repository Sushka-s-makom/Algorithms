"""QuickSort работает по принципу «разделяй и властвуй»:
Выбираем опорный элемент (pivot, «барьер»).
Разбиваем массив на элементы:
меньше pivot,
равные pivot (иногда выделяют отдельно),
больше pivot.
Рекурсивно сортируем левую и правую части.
Склеиваем результат."""
def quicksort_three_lists(a):
    if len(a) <= 1 :
        return a
    pivot = a[0]
    L, M, R = [], [], []

    for x in a :
        if x < a :
            L.append(x)
        elif x == pivot:
            M.append(x)
        else:
            R.append(x)
    return quicksort_three_lists(L) + M + quicksort_three_lists(R)
