class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        # Initialize the answer, current answer, start pointer, and number of zeroes in the window
        ans = current_ans = 0
        start = 0
        number_of_zeroes = 0

        # Helper function to check if the current window is valid
        def window_is_valid(t: int):
            return t <= k

        # Iterate through the array with the end pointer
        for end in range(len(nums)):
            # Increment the current answer length
            current_ans += 1
            # If the current element is zero, increment the number of zeroes in the window
            if not nums[end]:
                number_of_zeroes += 1

            # While the window is invalid, move the start pointer to the right
            while start <= end and not window_is_valid(number_of_zeroes):
                # If the element at the start pointer is zero, decrement the number of zeroes in the window
                if not nums[start]:
                    number_of_zeroes -= 1
                # Move the start pointer to the right and decrement the current answer length
                start += 1
                current_ans -= 1

            # Update the answer with the maximum length of a valid window
            ans = max(ans, current_ans)

        # Return the maximum length of a valid window
        return ans