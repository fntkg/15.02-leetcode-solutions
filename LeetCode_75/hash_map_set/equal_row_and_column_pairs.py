from collections import defaultdict


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        # Dictionary to count occurrences of each row
        row_counts = defaultdict(int)
        count = 0

        # Count each row's occurrences in the grid
        for row in grid:
            row_counts[tuple(row)] += 1

        # Count how many columns match any row
        for column in zip(*grid):
            count += row_counts[column]

        return count

if __name__ == "__main__":
    s = Solution()

    assert s.equalPairs([[3,2,1],[1,7,6],[2,7,7]]) == 1
    assert s.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]) == 3