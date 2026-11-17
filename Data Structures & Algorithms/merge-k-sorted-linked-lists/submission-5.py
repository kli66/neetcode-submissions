# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # forgot how to set a sorting key with heapify, returned to look it up 
        # turns out there is no such way, the items them selves have to be sortable
        # but also saw the merge method , but since we are aiming for a from scratch solution, did not use
        
        # did not see the reason for using a heap now? naive implementation could just iterate over the lists cross-sectionally? 
        heap_vals = []
        for idx, tmp in enumerate(lists):
            if tmp is not None:
                heap_vals.append((tmp.val, idx, tmp))
        heapq.heapify(heap_vals)
        
        head = ListNode()
        tail = head

        while heap_vals:
            nxt_val, idx, curr_head = heapq.heappop(heap_vals)
            tail.next = curr_head
            tail = curr_head
            if curr_head.next is not None:
                heapq.heappush(heap_vals, (curr_head.next.val, idx, curr_head.next))
        
        return head.next