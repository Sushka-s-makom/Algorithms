def get_hash(key, size):
    return hash(key) % size


def insert_linear(table, key, value):
    size = len(table)
    idx = get_hash(key, size)

    # Ищем свободное место (None) или обновляем старый ключ
    while table[idx] is not None:
        if table[idx][0] == key:
            break
        idx = (idx + 1) % size

    table[idx] = (key, value)


# Использование:
size = 10
my_table = [None] * size

insert_linear(my_table, "Python", 1991)
insert_linear(my_table, "Java", 1995)

print(my_table)