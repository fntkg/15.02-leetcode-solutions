class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Early exit for an empty list.
        if not nums:
            return 0

        # Cache the length of the list to avoid repeated len() calls.
        n = len(nums)
        j = 1  # j marks the position for the next unique element.

        # Iterate from the second element to the end.
        for i in range(1, n):
            # If the current element is different from the previous,
            # it is a unique element.
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1

        # j now represents the number of unique elements.
        return j
