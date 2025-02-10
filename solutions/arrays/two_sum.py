class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        """
        seen = {}
        for i, num in enumerate(nums):
            searched_value = target - num
            if searched_value in seen:
                return [seen[searched_value], i]
            seen[num] = i