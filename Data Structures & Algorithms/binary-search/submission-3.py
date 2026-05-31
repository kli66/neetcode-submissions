class Solution:
    def _search_with_idx(self, nums: list[int], target: int, left: int, right: int) -> int:
        mid = (left + right) // 2
        print(left, right , mid)
        if nums[mid] == target:
            return mid
        elif left == right:
            return -1
        elif nums[mid] < target:
            return self._search_with_idx(nums, target, min(mid + 1, len(nums)-1), right)
        else:
            return self._search_with_idx(nums, target, left, max(mid - 1, 0))


    def search(self, nums: List[int], target: int) -> int:
        return self._search_with_idx(nums, target, 0, len(nums) - 1)