import re
from collections import defaultdict


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        # Remove whitespaces, numbers and convert to lowercase
        cleaned_license_plate = re.sub(r'[\d\s]', '', licensePlate).lower()

        # Save each letter and its number of occurrences
        char_count = defaultdict(int)
        for char in cleaned_license_plate:
            char_count[char] += 1

        shortest_word = ""

        # For each word, check if it contains the letters in char_count with equal or more occurrences
        for word in words:
            word_char_count = char_count.copy()
            for char in word:
                # Check if each char is in char_count
                if char in word_char_count:
                    word_char_count[char] -= 1
            # If after processing the word, char_count is not zero, the word is not valid
            if not any(count > 0 for count in word_char_count.values()):
                # The word is valid, but we need to check if it is shorter
                if len(shortest_word) > len(word) or shortest_word == "":
                    shortest_word = word

        return shortest_word