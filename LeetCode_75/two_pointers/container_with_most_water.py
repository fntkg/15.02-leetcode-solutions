class Solution:
    def maxArea(self, height: list[int]) -> int:
        def container_area(heights: list[int], left: int, right: int) -> int:
            """
            Calculate the area of a rectangle formed by two lines.

            Args:
                heights (list[int]): A list of integers representing the heights of the lines.
                left (int): The index of the left line.
                right (int): The index of the right line.

            Returns:
                int: The area of a rectangle formed by two lines.
            """
            return (max(right, left) - min(right, left)) * min(heights[left], heights[right])

        # Initialize two pointers, one at the beginning and one at the end of the list
        i = 0
        j = len(height) - 1

        # Initialize the variable to store the maximum area found
        max_area = 0

        # Iterate while the left pointer is less than the right pointer
        while i < j:
            # Calculate the area formed by the lines at the current pointers
            area = container_area(height, i, j)

            # Update the maximum area if the current area is larger
            max_area = max(max_area, area)

            # Move the pointer which points to the lower height
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        # Return the maximum area found
        return max_area