import re


def Solution(s: str) -> bool:
    # First Solution
    s = s.lower()
    s = re.sub(r'\W+', '', s)
    # return s == s[::-1]

    s = s.lower()
    s = re.sub(r'\W+', '', s)
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left, right = left + 1, right - 1
    return True


# Time complexity: O(n)
# Space complexity: O(1)

# Test cases
assert Solution("A man, a plan, a canal: Panama") == True
assert Solution("race a car") == False
assert Solution("") == True
assert Solution("a") == True
assert Solution("aa") == True
assert Solution("ab") == False
assert Solution("aba") == True
assert Solution("abc") == False
assert Solution("abcba") == True
assert Solution("Able , was I saw Elba") == True
