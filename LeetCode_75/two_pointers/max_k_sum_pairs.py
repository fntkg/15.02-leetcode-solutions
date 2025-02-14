class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        # Initialize the variable to store the maximum number of operations
        max_operations = 0

        # Dictionary to store the count of each number in the list
        num_counts = {}

        # Iterate through each number in the list
        for num in nums:
            # Calculate the complement that would sum up to k
            complement = k - num

            # Check if the complement is already in the dictionary with a count greater than 0
            if num_counts.get(complement, 0) > 0:
                # If found, decrement the count of the complement
                num_counts[complement] -= 1
                # Increment the count of maximum operations
                max_operations += 1
            else:
                # If not found, increment the count of the current number in the dictionary
                num_counts[num] = num_counts.get(num, 0) + 1

        # Return the maximum number of operations found
        return max_operations