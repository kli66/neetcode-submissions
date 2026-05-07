class Solution:


    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # first brute force solution
        # sort the list of intervals by the left endpoint, 
        # then iterate the list of intervals beginning from the one with the left most start, merge as we continue

        # explicitly stating our sort criteria
        sorted_intervals = sorted(intervals, key=lambda x: (x[0], x[1]))

        # taken the leftmost interval as an example, the first interval after sorting that we find which has a left index > leftmost_interval's rightindex cannot be merged with the first one
        result = [sorted_intervals[0]]
        for left, right in sorted_intervals[1:]:
            last_right = result[-1][1]
            if left <= last_right:
                result[-1][1] = max(right, last_right)
            else:
                result.append([left, right])

        return result