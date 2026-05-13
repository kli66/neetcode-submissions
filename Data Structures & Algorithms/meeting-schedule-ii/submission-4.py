from _heapq import heappop
import heapq
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        # sort by meeting start point
        intervals.sort(key=lambda x: x.start)

        # so what structure do we want to use to hold the intervals?
        # we need:
        #   fast retrival based on end time, we only need the earliest one
        #   fast insertion
        # the first one suggests a minheap
        # initiate the min heap
        occupancy_heap: list[int] = []
        # seed the heap by pushing the earliest meeting to start
        heapq.heappush(occupancy_heap, intervals[0].end)
        # initiate a result var for return, already seeded
        max_room_count: int = 1
        # initiate a counter for the currently occupied rooms
        # may not need this, just use len()
        curr_room_count: int = 1

        # for each interval in meeting list, 
        # check the earliest end time of current already in a room
        # if the current interval's endtime is earlier than that, allocate a new room, advance the counter, compare and set the max for result
        # otherwise (>=), vacate the room with the earliest end time, decrease the counter
        for new_meeting in intervals[1:]:
            if new_meeting.start < occupancy_heap[0]:
                heapq.heappush(occupancy_heap, new_meeting.end)
                curr_room_count += 1
                max_room_count = max(max_room_count, curr_room_count)
                
            else:
                heapq.heappushpop(occupancy_heap, new_meeting.end)
        
        return max_room_count



