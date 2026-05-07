from itertools import permutations

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force
        pairs = permutations(nums, 2)
        for curr_pair in pairs:
            if curr_pair[0] + curr_pair[1] == target:
                break
        else:
            raise ValueError("Unexpected failure")
    
        print(curr_pair)
        # edge case - if both value are identical, then return the first two indicies found:
        if curr_pair[0] == curr_pair[1]:
            idx_1 = nums.index(curr_pair[0])
            # we should be able to guarantee idx_1 existence
            del(nums[idx_1])

            idx_2 = nums.index(curr_pair[1]) + 1

        else:
            idx_1 = nums.index(curr_pair[0])

            idx_2 = nums.index(curr_pair[1])

        return [idx_1, idx_2]