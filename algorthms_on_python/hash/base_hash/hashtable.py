from rolling_hash_func import fast_calc_hash
MOD32 = 2**32

def ht_create(m: int = 8):
    return {
        "m": m, #размер массива бакетов
        "n": 0, #сколько элементов реально лежит
        "buckets": [[] for _ in range(m)] #список списков
    }

def ht_index(ht, key):
    h = fast_calc_hash(key)
    return h % ht["m"]

def ht_set(ht, key, value):
    idx = ht_index(ht, key)
    bucket = ht["buckets"][idx]

    # если ключ уже есть - обновляем
    for i, (k, _) in enumerate(bucket):
        if k == key:
            bucket[i] = (key, value)
            return
    #иначе
    bucket.append((key, value))
    ht["n"] += 1

def ht_get(ht, key, default=None):
    idx = ht_index(ht, key)
    bucket = ht["buckets"][idx]

    for k, v in bucket:
        if k == key:
            return v
    return default

def ht_delete(ht, key: int) -> bool:
    idx = ht_index(ht, key)
    bucket = ht["buckets"][idx]

    for i, (k, _) in enumerate(bucket):
        if k == key:
            bucket.pop(i)
            ht["n"] -= 1
            return True
    return False



