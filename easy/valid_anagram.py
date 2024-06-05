class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1

        return s_dict == t_dict


# Time complexity: O(n)
# Space complexity: O(n)

# Path: easy/valid_anagram.py

# Test cases
s = Solution()
assert s.isAnagram("anagram", "nagaram") == True
assert s.isAnagram("rat", "car") == False
assert s.isAnagram("a", "ab") == False
assert s.isAnagram("ab", "a") == False
assert s.isAnagram("ab", "ba") == True
assert s.isAnagram("", "") == True
assert s.isAnagram("a", "a") == True
assert s.isAnagram("a", "b") == False
assert s.isAnagram("abc", "cba") == True
assert s.isAnagram("abc", "bca") == True
assert s.isAnagram("abc", "cab") == True
assert s.isAnagram("abc", "bac") == True
assert s.isAnagram("abc", "acb") == True
assert s.isAnagram("abc", "cab") == True
