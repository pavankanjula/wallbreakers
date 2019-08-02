class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Time - O(numCourses + len(prerequisites))
        # Space - O(numCourses + len(prerequisites))
        if numCourses == 1:
            return True
        adj_list = {}  # To build a graph data structure from the given information
        # Each key in adj_list is a course and it's value is a list containing the courses which should be completed only after this course.
        for i in range(numCourses):
            adj_list[i] = []
        for pair in prerequisites:
            adj_list[pair[1]].append(pair[0])
        # Main idea is to detect if there is any cycle and return True if no cycle is detected.
        visited = set()  # Tracks all the courses after visiting once to reduce repititive work.
        for course in adj_list.keys():  # check cycle for each course
            if not course in visited:
                if self.DFS(course, adj_list, visited, set()):
                    return False
        return True

    def DFS(self, course, adj_list, visited, cur_path):
        # Cycle detection using Depth first search
        if course in cur_path:  # cur_path stores all the courses in the path currently traversing. So if we find a course which we came across already, it is a cycle.
            return True
        if course in visited:
            return False
        visited.add(course)
        cur_path.add(course)
        for nbr in adj_list[course]:  # check if any of it's neighbours has cycles.
            if nbr in cur_path:
                return True
            if not nbr in visited and self.DFS(nbr, adj_list, visited, cur_path):
                return True
        # if we reach here, we didn't find any cycle so we can remove it from the current path.
        cur_path.remove(course)
        return False