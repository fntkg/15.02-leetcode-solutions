class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # If the input list is empty, return an empty string
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        # Initialize binary search boundaries
        left = 0
        right = min(map(len, strs))# The shortest string length determines the max possible prefix

        # Function to check if all strings share a common prefix of a given length
        def is_common_prefix(length: int) -> bool:
            return all(s.startswith(strs[0][:length]) for s in strs)

        # Perform binary search to find the longest common prefix
        while left <= right:
            mid = (left + right) // 2  # Middle index of the current search range

            if is_common_prefix(mid):
                # If all strings have a common prefix of length 'mid', search in the right half
                left = mid + 1
            else:
                # Otherwise, search in the left half
                right = mid - 1

        # The longest common prefix length is (left + right) // 2
        return strs[0][:right]

if __name__ == "__main__":
    s = Solution()

    assert s.longestCommonPrefix(["flower","flow","flight"]) == "fl"
    assert s.longestCommonPrefix(["dog","racecar","car"]) == ""
    assert s.longestCommonPrefix(["c","acc","ccc"]) == ""