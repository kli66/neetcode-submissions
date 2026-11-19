import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = bisect.bisect_left(nums, target)
        print(lower)
        if  lower >= len(nums) or nums[lower] != target:
            return -1
        else:
            return lower