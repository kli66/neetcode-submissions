import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * tmp for tmp in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            
            tmp_1 = heapq.heappop(stones)
            tmp_2 =  heapq.heappop(stones)
            if tmp_1 == tmp_2:
                continue
            else:
                heapq.heappush(stones, abs(tmp_1 - tmp_2)*-1)
        
        return -1 * stones.pop() if stones else 0