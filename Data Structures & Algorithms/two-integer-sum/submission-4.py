class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # one pass solution
        # maps nums value to index
        idx_map: dict[int:int] = {}

        for idx, value in enumerate(nums):
            if (target - value ) in idx_map:
                return [idx_map.get(target - value), idx]
            else:
                idx_map[value] = idx
        else:
            raise ValueError("Unexpected input, no result found")