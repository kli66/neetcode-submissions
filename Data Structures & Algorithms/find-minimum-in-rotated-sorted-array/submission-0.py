# theory - find the first inversion/non order idx, smallest is on the right side


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1
        while l < r:
            mid = l + (r-l)//2 

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        return nums[l]

'''
3, 4, 5, 6, 1, 2]
[612] 
[6,1]

'''