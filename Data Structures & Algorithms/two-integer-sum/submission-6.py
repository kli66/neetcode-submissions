
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {x : idx for idx, x in enumerate(nums)}

        for idx, x in enumerate(nums):
            if target - x in complement:
                comp_idx = complement[target-x]
                if comp_idx != idx:
                    return sorted([idx, complement[target-x]])
        else:
            raise Exception
