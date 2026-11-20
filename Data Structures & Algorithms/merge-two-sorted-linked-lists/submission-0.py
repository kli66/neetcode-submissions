from _heapq import heappush
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        
        head = ListNode()
        curr_head = ListNode()
        head.next = curr_head
        chain = []
        for (idx, node) in enumerate([list1, list2]):
            if node is not None:
                heapq.heappush(chain, (node.val, idx, node))

        while chain:
            val, idx, curr_node = heapq.heappop(chain)
            curr_head.next = curr_node
            curr_head = curr_node
            if curr_node.next is None:
                continue
            else:
                heapq.heappush(chain, (curr_node.next.val, idx, curr_node.next))

        return head.next.next