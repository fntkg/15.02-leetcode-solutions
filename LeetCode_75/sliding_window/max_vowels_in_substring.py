class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Initialize the current number of vowels and the maximum number of vowels found in any substring
        current_num_vowels = max_num_vowels = 0
        # Define a set of vowels for quick lookup
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # Iterate through the string with index and character
        for i, char in enumerate(s):
            # If the character is a vowel, increment the current number of vowels
            if char in vowels:
                current_num_vowels += 1
            # If the index is greater than or equal to 'k', check the character 'k' positions back
            # If it is a vowel, decrement the current number of vowels
            if i >= k and s[i - k] in vowels:
                current_num_vowels -= 1
            # Update the maximum number of vowels found
            max_num_vowels = max(max_num_vowels, current_num_vowels)

        # Return the maximum number of vowels found in any substring of length 'k'
        return max_num_vowels