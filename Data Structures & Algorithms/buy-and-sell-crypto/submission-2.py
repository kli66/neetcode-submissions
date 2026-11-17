

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low_idx = 0
        high_idx = 1
        profit = 0
        # loop condition unsure
        while high_idx < len(prices):
            if prices[low_idx] > prices[high_idx]:
                # we always keep low at global low
                low_idx = high_idx
                high_idx += 1
            else:
                new_profit = prices[high_idx] - prices[low_idx]
                if new_profit > profit:
                    profit = new_profit
                    # since low is at global low always, we know that the high price moved, so only moves high idx
                high_idx += 1

        return profit