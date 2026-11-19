# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result_head  = ListNode()
        curr_head = result_head

        heap = []
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, idx, node))

        while heap:
            val, idx, curr = heapq.heappop(heap)
            if curr.next is not None:
                heapq.heappush(heap, (curr.next.val, idx, curr.next))
            curr_head.next = curr
            curr_head = curr
        
        return result_head.next if result_head.next is not None else None
            
