class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = dict()

        for curr in nums:
            result[curr] = result.get(curr, 0) + 1

        flattened = list(zip(result.values(), result.keys()))
        heapq.heapify(flattened)
    
        return [tmp[1] for tmp in heapq.nlargest(k, flattened)]