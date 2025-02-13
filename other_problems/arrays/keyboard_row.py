class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        # Define sets for each row of the keyboard
        row_1 = set("qwertyuiop")
        row_2 = set("asdfghjkl")
        row_3 = set("zxcvbnm")

        # Initialize an empty list to store the result
        result = []

        # Iterate over each word in the input list
        for word in words:
            # Convert the word to lowercase and create a set of its characters
            w = set(word.lower())
            # Check if all characters of the word are in any one row (check w is a subset of row_x)
            if w <= row_1 or w <= row_2 or w <= row_3:
                # Append the word to the result list if the condition is met
                result.append(word)

        # Return the list of words that can be typed using letters of one row
        return result