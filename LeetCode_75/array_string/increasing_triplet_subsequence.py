class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        """
        Given an integer array nums, return true if there exists a triple of
        indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
        If no such indices exists, return false.
        """
        # Initialize two variables to track the smallest and second smallest numbers
        first = second = float('inf')
        for n in nums:
            # Update the smallest number if the current number is smaller or equal
            if n <= first:
                first = n
            # Update the second smallest number if the current number is smaller or equal
            # but greater than the smallest number
            elif n <= second:
                second = n
            # If we find a number greater than both, we have an increasing triplet
            else:
                return True
        # If no increasing triplet is found, return False
        return False