
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lo = 0
        hi = 0
        profit = 0

        while hi < len(prices):
            if prices[lo] >= prices[hi]:
                lo = hi
            else:
                profit += prices[hi] - prices[lo]
                lo = hi
                print(lo, hi, profit)
            hi += 1
        return profit