class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        """
        # Initialize a dictionary to store the indices of the numbers we have seen so far
        seen = {}
        # Iterate over the list of numbers with their indices
        for i, num in enumerate(nums):
            # Calculate the value needed to reach the target sum
            searched_value = target - num
            # Check if the needed value is already in the dictionary
            if searched_value in seen:
                # If found, return the indices of the current number and the needed value
                return [seen[searched_value], i]
            # Otherwise, add the current number and its index to the dictionary
            seen[num] = i