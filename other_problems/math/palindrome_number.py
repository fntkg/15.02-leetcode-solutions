class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Given an integer x, return true if x is a palindrome, and false otherwise.
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_num = 0
        original = x

        while original > reversed_num:
            reversed_num = reversed_num*10 + original % 10
            original = original // 10

        return original == reversed_num or original == reversed_num // 10
