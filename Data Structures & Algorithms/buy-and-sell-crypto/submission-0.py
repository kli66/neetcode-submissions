

class Solution:

    @staticmethod
    def best_given_price(bought: int, fut_prices: List[int]) -> int:
        return max(fut_prices) - bought



    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        max_idx = len(prices) - 1
        for idx in range(len(prices)):
            if idx == max_idx:
                break
            curr_best = self.best_given_price(prices[idx], prices[idx+1:])
            result = max(curr_best, result)
        
        return result 