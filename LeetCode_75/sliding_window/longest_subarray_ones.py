class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        # Initialize the answer, current answer, start pointer, and number of zeroes in the window
        ans = current_ans = 0
        start = 0
        deleted_zeroes = 0

        # Helper function to check if the current window is valid
        def window_is_valid(n: int) -> bool:
            return n <= 1

        # Iterate through the array with the end pointer
        for end in range(len(nums)):
            # Increment the current answer length
            current_ans += 1
            # If the current element is zero, increment the number of zeroes in the window
            if not nums[end]:
                deleted_zeroes += 1

            # While the window is invalid, move the start pointer to the right
            while start <= end and not window_is_valid(deleted_zeroes):
                # If the element at the start pointer is zero, decrement the number of zeroes in the window
                if not nums[start]:
                    deleted_zeroes -= 1
                # Move the start pointer to the right and decrement the current answer length
                start += 1
                current_ans -= 1

            # Update the answer with the maximum length of a valid window
            ans = max(ans, current_ans)

        # Return the maximum length of a valid window
        return ans-1

if __name__ == "__main__":
    solution = Solution()
    print(f'Test A: {solution.longestSubarray([1,1,0,1])} -- expected: 3')
    print(f'Test B: {solution.longestSubarray([0,1,1,1,0,1,1,0,1])} -- expected: 5')
    print(f'Test C: {solution.longestSubarray([1,1,1])} -- expected: 2')