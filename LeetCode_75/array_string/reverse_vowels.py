class Solution:
    def reverseVowels(self, s: str) -> str:
        # Set of vowels for quick lookup
        vowels = set('aeiouAEIOU')

        # Initialize two pointers
        i, j = 0, len(s) - 1
        # Convert the string to a list to allow modification
        result = list(s)

        # Loop until the two pointers meet
        while i < j:
            # If both pointers point to vowels, swap them
            if result[i] in vowels and result[j] in vowels:
                result[i], result[j] = result[j], result[i]
                i += 1
                j -= 1
            # Move the left pointer to the right if it's not a vowel
            if result[i] not in vowels:
                i += 1
            # Move the right pointer to the left if it's not a vowel
            if result[j] not in vowels:
                j -= 1

        # Join the list back into a string and return it
        return "".join(result)