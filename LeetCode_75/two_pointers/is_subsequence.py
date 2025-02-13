class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Initialize two pointers: i for the current character in s, j for the current character in t
        i, j = 0, 0

        # Iterate through t while there are characters left in both s and t
        while j < len(t) and i < len(s):
            if t[j] == s[i]:
                # If characters match, move to the next character in s
                i += 1
            # Always move to the next character in t
            j += 1

        # If all characters in s were found in t in order, return True
        return i == len(s)
