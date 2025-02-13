class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the input string into words
        words = s.split()  # ["the", "sky", "is", "blue"]

        # Initialize an empty list to store the reversed words
        reversed_words = []

        # Iterate over the words list in reverse order
        for i in range(len(words) - 1, -1, -1):
            # Append each word to the reversed_words list
            reversed_words.append(words[i])

        # Join the reversed words with a space and return the result
        return " ".join(reversed_words)