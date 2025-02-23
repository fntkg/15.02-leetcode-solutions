class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        Given an integer array `nums` and an integer `val`, remove all occurrences of `val`
        in-place. The order of the elements may be changed.
        Return the new length of the array containing only the elements that are not equal to `val`.

        This optimized approach uses two pointers:
          - Pointer `i` iterates from the beginning of the list.
          - `n` represents the effective length of the list.
        If nums[i] equals `val`, we swap it with the element at index `n - 1` and decrease `n`.
        If not, we simply move `i` forward.
        This process continues until `i` reaches `n`, ensuring that all unwanted values
        are moved past the new end of the array.
        """
        i = 0  # Start pointer at the beginning.
        n = len(nums)  # `n` represents the current effective length of the list.

        # Iterate until i reaches the effective length.
        while i < n:
            if nums[i] == val:
                # Replace nums[i] with the last element in the current range.
                nums[i] = nums[n - 1]
                # Decrease the effective length since the last element is now out of consideration.
                n -= 1
                # Do not increment i here because the new element at nums[i] must be checked.
            else:
                # If the current element is not `val`, move to the next element.
                i += 1

        # After processing, `n` is the number of elements not equal to `val`.
        return n
