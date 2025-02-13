class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize two pointers: current for the current number and next_non_zero for the next non-zero number
        current, next_non_zero = 0, 1
        n = len(nums)

        while next_non_zero < n:
            if nums[current] == 0:
                if nums[next_non_zero] == 0:
                    # Move next_non_zero until you find a non-zero number
                    while next_non_zero < n and nums[next_non_zero] == 0:
                        next_non_zero += 1
                if next_non_zero < n:
                    # Swap the zero at current with the non-zero number at next_non_zero
                    nums[current], nums[next_non_zero] = nums[next_non_zero], nums[current]
            # Move both pointers forward
            current += 1
            next_non_zero += 1