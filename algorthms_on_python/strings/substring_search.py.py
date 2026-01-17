"""
Algorithm: Naive substring search (all occurrences)

Finds all starting positions where `sub` occurs in string `s`.

Idea:
- Move a window of length m over s.
- Compare s[i:i+m] with sub.
- If equal -> add i to positions.

Time complexity:
    Worst: O((n - m + 1) * m)  ~ O(n*m)
    (because slicing + equality check both may take O(m))
Space complexity:
    O(k) for output positions, where k is number of occurrences
    + O(m) temporary slice (created each iteration)

Notes:
- This is an educational baseline. For faster search, there are KMP/Z-algorithm, etc.
"""

from equal import equal


def search_substring(s: str, sub: str) -> list[int]:
    n, m = len(s), len(sub)
    pos = []

    # Convention: empty substring occurs at every position (including at the end)
    if m == 0:
        return list(range(n + 1))

    if m > n:
        return []

    for i in range(0, n - m + 1):
        if equal(s[i:i + m], sub):
            pos.append(i)

    return pos
def test_search_substring():
    print("test_case #1:", end=" ")
    print("Ok" if search_substring("abracadabra", "abra") == [0, 7] else "Fail")

    print("test_case #2:", end=" ")
    print("Ok" if search_substring("aaaaa", "aa") == [0, 1, 2, 3] else "Fail")

    print("test_case #3:", end=" ")
    print("Ok" if search_substring("hello", "world") == [] else "Fail")

    print("test_case #4:", end=" ")
    print("Ok" if search_substring("abc", "abc") == [0] else "Fail")

    print("test_case #5:", end=" ")
    print("Ok" if search_substring("abc", "") == [0, 1, 2, 3] else "Fail")

    print("test_case #6:", end=" ")
    print("Ok" if search_substring("", "a") == [] else "Fail")

    print("test_case #7:", end=" ")
    print("Ok" if search_substring("", "") == [0] else "Fail")


if __name__ == "__main__":
    print(search_substring("abracadabra", "abra"))
    test_search_substring()
