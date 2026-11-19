class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_req_cnt = {curr:0 for curr in range(numCourses)}
        rev_prereq_list = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            pre_req_cnt[course] += 1
            rev_prereq_list[prereq].append(course)
        
        todo = [course for course in range(numCourses) if pre_req_cnt[course] == 0]

        seq = []
        while todo:
            next_course = todo.pop()
            seq.append(next_course)

            for prereq in rev_prereq_list[next_course]:
                pre_req_cnt[prereq] -= 1
                if pre_req_cnt[prereq] == 0:
                    todo.append(prereq)
        
        if len(seq) == numCourses:
            return seq
        else:
            return []
