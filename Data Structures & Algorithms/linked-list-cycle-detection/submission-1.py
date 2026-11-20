# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        slow = head
        if slow is None:
            return False

        fast = slow.next
        
        while slow is not None and fast is not None:
            slow = slow.next
            next_fast = fast.next 
            next_fast = next_fast.next if next_fast is not None else None
            fast = next_fast
            if fast == slow:
                return True
        
        return False