# brute force solution



class Solution:



    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        curr_left = 0
        curr_right = curr_left + k
        result = []
        while curr_left <= len(nums) - k:
            result.append(max(nums[curr_left:curr_right]))
        
            curr_left += 1
            curr_right += 1
        
        return result
