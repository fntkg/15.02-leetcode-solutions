class Solution:
    def compress(self, chars: list[str]) -> int:
        # Initialize pointers for the current position in the input list and the result position
        i = 0
        res = 0

        # Iterate through the characters in the list
        while i < len(chars):
            # Initialize the length of the current group of identical characters
            group_length = 1

            # Count the number of identical characters in the current group
            while i + group_length < len(chars) and chars[i + group_length] == chars[i]:
                group_length += 1

            # Place the current character in the result position
            chars[res] = chars[i]
            res += 1

            # If the group length is greater than 1, convert the length to a string and place it in the result
            if group_length > 1:
                str_repr = str(group_length)
                chars[res:res + len(str_repr)] = list(str_repr)
                res += len(str_repr)

            # Move to the next group of characters
            i += group_length

        # Return the length of the compressed list
        return res
