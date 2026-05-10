"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        if len(intervals) == 0:
            return 0

        sorted_start: list[int] = sorted([tmp.start for tmp in intervals])
        sorted_end: list[int] = sorted([tmp.end for tmp in intervals])

        result = 0
        count = 0
        s_pos = 0
        e_pos = 0
        while s_pos < len(intervals):
            if sorted_start[s_pos] < sorted_end[e_pos]:
                count += 1
                s_pos += 1
            else:
                e_pos += 1
                count -= 1
            
            result = max(count, result)

        return result
