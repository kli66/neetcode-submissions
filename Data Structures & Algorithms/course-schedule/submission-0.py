"""
Kahn's solution - looked up algo definition (not concrete implementation) beforehand
"""
from collections import Counter, deque, defaultdict

# The pair [0, 1], indicates that must take course 1 before taking course 0.


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependants = Counter()
        dependencies = defaultdict(list)
        to_do = deque()

        for curr, prereq in prerequisites:
            dependants[prereq] += 1
            dependencies.setdefault(curr, []).append(prereq)
        
        for curr in range(numCourses):
            if dependants[curr] == 0:
                to_do.append(curr)
        
        finish_cnt = 0
        while to_do:
            new_finished = to_do.pop()
            finish_cnt += 1
            for curr_dep in dependencies[new_finished]:
                dependants[curr_dep] -= 1
                if dependants[curr_dep] == 0:
                    to_do.append(curr_dep)

        return finish_cnt == numCourses
        

