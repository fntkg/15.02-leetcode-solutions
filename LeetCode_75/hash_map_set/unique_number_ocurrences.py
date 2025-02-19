class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        # Dictionary to count occurrences of each element
        a = {}

        # Count occurrences of each element in the array
        for n in arr:
            a[n] = a.get(n, 0) + 1

        # Check if all occurrence counts are unique
        return len(a) == len(set(a.values()))

if __name__ == "__main__":
    solution = Solution()
    print(f'Test A: {solution.uniqueOccurrences([1,2,2,1,1,3])} -- expected: true')