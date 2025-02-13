class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n  # Initialize the result array with 1s
        prefix, suffix = 1, 1  # Variables to keep track of prefix and suffix products

        # Compute prefix and suffix products in a single pass
        for i in range(n):
            result[i] *= prefix  # Multiply the current index by the prefix product
            prefix *= nums[i]  # Update the prefix product

            result[-1 - i] *= suffix  # Multiply the mirrored index by the suffix product
            suffix *= nums[-1 - i]  # Update the suffix product

        return result
