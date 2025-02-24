class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Sort the list so that identical elements are adjacent.
        nums.sort()
        # The majority element appears more than n/2 times,
        # so it must occupy the middle position in the sorted list.
        return nums[len(nums) // 2]


if __name__ == "__main__":
    s = Solution()

    assert s.majorityElement([6,5,5]) == 5
    assert s.majorityElement([3,2,3]) == 3