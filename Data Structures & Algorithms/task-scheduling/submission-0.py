import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # max heap for tracking task id and its leftover frequency
        task_counts = Counter(tasks)
        task_heap = [-cnt for cnt in task_counts.values()]
        heapq.heapify(task_heap)
        del task_counts
        
        # task queue with remaining count and next avaialble time
        task_queue: deque[tuple[int, int]] = deque()

        # timer for tracking currently elapsed time
        time = 0

        while task_heap or task_queue:
            time += 1
            if not task_heap:
                time = task_queue[0][1]
            else:
                count = -1 * heapq.heappop(task_heap)
                count -= 1

                if count > 0:
                    task_queue.append((count, time + n))

            if task_queue and task_queue[0][1] == time:
                read_task = task_queue.popleft()
                heapq.heappush(task_heap, -1 * read_task[0])
        
        return time 