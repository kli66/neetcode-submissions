import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def eulc_dist(x, y):
            return x**2 + y**2
        
        result = []
        for point in points:
            if len(result) < k:
                heapq.heappush(result, (-1 * eulc_dist(*point), point))
            else:
                heapq.heappushpop(result, (-1 * eulc_dist(*point), point))

        return [tmp[1] for tmp in result]        
