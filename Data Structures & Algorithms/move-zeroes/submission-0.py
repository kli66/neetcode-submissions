class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0

        # right always races forward to find the non-zero element
        for r in range(len(nums)):

            # critical state check, until r points to a none zero element, l and r grows together
            # when r points to a zero position, l would stop while r advances.
            # then, when r finally encounters the next none zero element, l is still at the position where 
            # the first zero is encounterd, hence enabling the swap.
            if nums[r] != 0:
                # if not pointing to the same location, means l must be in a zero state, swap
                if l!= r:
                    nums[l], nums[r] = nums[r], nums[l]
                    
                # l should maintain the leftmost zero position 
                l+=1    