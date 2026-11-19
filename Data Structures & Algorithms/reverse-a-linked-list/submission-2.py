# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    did not solve in 7 minutes, looked up prev solutions, very frustrating 
    ruminations returned because I could not solve the easy question in one try. 
    need some adjustments
    """

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        
    
        return prev