class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Operation 1 allows you to freely reorder the string. -> We can use sets or dictionary as order doesn't matter
        # Operation 2 allows you to freely reassign the letters' frequencies. -> We need to care about frequencies so we need to use a dict

        # Create a frequency dictionary for word1
        freq_1 = {}
        for char in word1:
            freq_1[char] = freq_1.get(char, 0) + 1

        # Create a frequency dictionary for word2
        freq_2 = {}
        for char in word2:
            freq_2[char] = freq_2.get(char, 0) + 1

        # Check if both words have the same length, the same frequency values, and the same set of characters
        return len(word1) == len(word2) and sorted(freq_1.values()) == sorted(freq_2.values()) and sorted(freq_1.keys()) == sorted(freq_2.keys())