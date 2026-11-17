import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = heapq.nlargest(k, nums)
        print(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        print(self.nums)
        self.nums = heapq.nlargest(self.k, self.nums)
        print(self.nums)

        return self.nums[-1]

