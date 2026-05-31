class Solution:
    def _search_with_idx(self, nums: list[int], target: int, left: int, right: int) -> int:
        if left > right:
            return -1
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self._search_with_idx(nums, target, mid+1, right)
        else:
            return self._search_with_idx(nums, target, left, mid-1)

    def search(self, nums: List[int], target: int) -> int:
        return self._search_with_idx(nums, target, 0, len(nums) - 1)