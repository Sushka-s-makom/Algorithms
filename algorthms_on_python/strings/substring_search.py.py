from equal import equal
def search_substring(s: str, sub: str) -> list[int]:
    n, m = len(s), len(sub)
    pos = []
    for i in range(0, n - m + 1):
        if equal(s[i:i+m], sub):
            pos.append(i)
    return pos