def calc_hash(data):
    k = 3571
    s = 0
    i = 1
    data += 8233293
    while data > 0:
        s += (data % 2) * (k**i)
        i += 1
        data //= 2
    return s % 2 ** 32

def fast_calc_hash(data):
    k = 3571
    MOD = 2 ** 32
    data += 8233293
    s = 0
    p = k
    while data > 0:
        bit = data & 1  # быстрее чем data % 2
        s = (s + bit * p) % MOD
        p = (p * k) % MOD  # следующий k**(i+1)
        data >>= 1  # быстрее чем data //= 2
    return s

