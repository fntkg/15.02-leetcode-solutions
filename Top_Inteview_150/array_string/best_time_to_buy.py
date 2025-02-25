class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Initialize buy_price to a very high value so that any price in the list will be lower.
        buy_price = float('inf')
        # Initialize max_profit to 0 as we start with no profit.
        max_profit = 0

        for price in prices:
            # Update buy_price with the smallest value seen so far.
            buy_price = min(buy_price, price)
            # Calculate the profit if selling at the current price after buying at buy_price,
            # then update max_profit if this profit is greater than the previous max_profit.
            max_profit = max(max_profit, price - buy_price)

        # Return the maximum profit achievable.
        return max_profit


if __name__ == "__main__":
    s = Solution()

    assert s.maxProfit([7,1,5,3,6,4]) == 5
    assert s.maxProfit([2,4,1]) == 2
    assert s.maxProfit([3,2,6,5,0,3]) == 4