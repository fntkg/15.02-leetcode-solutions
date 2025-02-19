class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans_1 = []  # List of integers in nums1 which are not present in nums2
        ans_2 = []  # List of integers in nums2 which are not present in nums1
        # As we don't care about order or repetitions we can use sets.
        set_1 = set(nums1)
        set_2 = set(nums2)

        for num in set_1:
            if num not in set_2:
                ans_1.append(num)

        for num in set_2:
            if num not in set_1:
                ans_2.append(num)

        return [ans_1, ans_2]