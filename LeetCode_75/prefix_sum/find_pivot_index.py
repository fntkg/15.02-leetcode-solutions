class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
       # Initialize the sum of elements to the left of the current index to 0
       sum_left = 0
       # Calculate the total sum of the array elements
       sum_right = sum(nums)

       # Iterate through the array with both index and element
       for i, num in enumerate(nums):
           # Subtract the current element from the right sum
           sum_right -= num

           # Check if the left sum is equal to the right sum
           if sum_left == sum_right:
               # If they are equal, return the current index
               return i

           # Add the current element to the left sum
           sum_left += num

       # If no pivot index is found, return -1
       return -1