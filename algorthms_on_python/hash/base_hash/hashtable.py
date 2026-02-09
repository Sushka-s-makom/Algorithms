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

