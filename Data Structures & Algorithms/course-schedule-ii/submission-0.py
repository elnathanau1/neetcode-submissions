from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_map = {}
        for num in range(numCourses):
            course_map[num] = [set(), set()] # first for next node, second for prereqs

        for curr, prereq in prerequisites:
            course_map[prereq][0].add(curr)
            course_map[curr][1].add(prereq)

        queue = deque()

        for course in [x for x in course_map.keys() if len(course_map[x][1]) == 0]:
            queue.append(course)
        
        ret_list = []
        while queue:
            course = queue.popleft()
            ret_list.append(course)
            for nxt in course_map[course][0]:
                course_map[nxt][1].discard(course)
                if len(course_map[nxt][1]) == 0:
                    queue.append(nxt)

        if len(ret_list) == numCourses:
            return ret_list
        return []