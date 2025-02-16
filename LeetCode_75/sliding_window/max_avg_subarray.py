class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Initialize the maximum sum and the current sum of the first 'k' elements
        max_sum = sum_total = sum(nums[:k])

        # Iterate through the array starting from the 'k'th element
        for i in range(k, len(nums)):
            # Update the current sum by adding the next element and subtracting the element 'k' positions back
            sum_total += nums[i] - nums[i - k]
            # Update the maximum sum if the current sum is greater
            max_sum = max(max_sum, sum_total)

        # Return the maximum average by dividing the maximum sum by 'k'
        return max_sum / k