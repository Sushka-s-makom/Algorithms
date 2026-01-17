"""
Algorithm: String equality check (character-by-character)

Checks whether two strings A and B are equal.

Idea:
1) If lengths differ, strings are not equal.
2) Compare characters at the same positions one by one.
3) If all characters match, strings are equal.

Time complexity:
    O(n), where n = len(A)
Space complexity:
    O(1)
"""

def equal(A: str, B: str) -> bool:
    if len(A) != len(B):
        return False

    for i in range(len(A)):
        if A[i] != B[i]:
            return False

    return True



