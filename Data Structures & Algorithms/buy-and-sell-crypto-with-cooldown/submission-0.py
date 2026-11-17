# ashamed - took me about 30 minutes to realize that I have to add the current round of profit to cached value 
# main 


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = dict()

        def calc_profit(lo, hi, profit):
            """
            returns the max future profit starting from lo and hi
            """
            if not len(prices) > hi:
                return profit
            
            # inversion, move the window forward
            if prices[lo] >= prices[hi]:
                return cache.get((hi, hi + 1)) or calc_profit(hi, hi + 1, profit)

            # (0,2) (0,3) (0,4)
            hold_profit = cache.get((lo, hi + 1)) or calc_profit(lo, hi + 1, profit)
            trade_profit = prices[hi] - prices[lo] + (cache.get((hi + 2, hi + 3)) or calc_profit(
                hi + 2, hi + 3, profit
            ))

            result = profit + max(hold_profit, trade_profit)
            cache[(lo, hi)] = max(result, cache.get((lo,hi), 0))
            return result

        return calc_profit(0, 0, 0)
