class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # Initialize three pointers:
        # p1: points to the last valid element in nums1 (i.e., index m-1)
        # p2: points to the last element in nums2 (i.e., index n-1)
        # p: points to the last index of nums1 (i.e., index m+n-1)
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        # Merge nums1 and nums2 starting from the end
        # This avoids overwriting elements in nums1 that haven't been checked yet.
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]  # Place the larger element at the end of nums1
                p1 -= 1
            else:
                nums1[p] = nums2[p2]  # Place the larger element at the end of nums1
                p2 -= 1
            p -= 1

        # If there are remaining elements in nums2, copy them.
        # No need to do anything for nums1 because they are already in place.
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1