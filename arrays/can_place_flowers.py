class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        def can_plant(i):
            # Check if the current plot is empty, and its neighbors are empty (or non-existent)
            return (flowerbed[i] == 0 and
                    (i == 0 or flowerbed[i - 1] == 0) and
                    (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0))

        for i in range(len(flowerbed)):  # Iterate over the entire list
            if n > 0 and can_plant(i):
                flowerbed[i] = 1  # Plant a flower
                n -= 1
                if n == 0:
                    break
                # Skip the next plot to avoid adjacent plantings:
                i += 1

        return n <= 0  # True if all flowers were planted, else False