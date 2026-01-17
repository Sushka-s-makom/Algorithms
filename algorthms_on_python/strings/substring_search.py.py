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


