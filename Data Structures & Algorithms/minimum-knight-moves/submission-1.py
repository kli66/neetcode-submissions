# with help from bot -  did not realize that we can keep visited set and symmetiricity
from collections import deque

DIR = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-2, -1), (-1, -2)]

def gen_targets(sr, sc, cost):
    return [(sr + dx, sc + dy, cost + 1) for dx, dy in DIR]

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        targets = deque([(0, 0, 0)])
        visited = set([(0, 0)])
        
        # BFS till x,y
        while targets:
            sr, sc, cost = targets.popleft()
            if (sr, sc) == (x, y):
                return cost

            for nxt_r, nxt_c, nxt_cost in gen_targets(sr, sc, cost):
                # note the additional range check against target (x,y) , nice
                # 
                if (nxt_r, nxt_c) not in visited and -2 <= nxt_r <= x + 2 and -2 <= nxt_c <= y + 2:
                    visited.add((nxt_r, nxt_c))
                    targets.append((nxt_r, nxt_c, nxt_cost))
