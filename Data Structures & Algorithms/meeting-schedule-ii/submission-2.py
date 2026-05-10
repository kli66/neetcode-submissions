"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        if not intervals:
            return 0

        sorted_meetings = sorted(intervals, key=lambda x: x.start)

        free_rooms = []

        heapq.heappush(free_rooms, sorted_meetings[0].end)

        for curr_meeting in sorted_meetings[1:]:
            if curr_meeting.start >= free_rooms[0]:
                heapq.heappop(free_rooms)

            heapq.heappush(free_rooms, curr_meeting.end)

        return len(free_rooms)
