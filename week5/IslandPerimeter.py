class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Time - O(m*n) ; m is length of rows and n is length of columns
        # Space - O(m*n) ; To store the queue
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        start = None  # To find the start of island
        found = False  # if found becomes true, we can stop the loop
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start = (i, j)
                    found = True
                    break
            if found == True:
                break

        # BFS starts here
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 4 directions
        perimeter = 0
        visited = set()  # To track visited nodes
        queue = collections.deque()
        queue.append(start)
        while queue:
            x, y = queue.pop()
            if not (x, y) in visited:
                visited.add((x, y))
                cur_pmtr = 4  # for any position perimeter will be 4
                for i, j in directions:
                    if x + i >= 0 and x + i < len(grid) and y + j >= 0 and y + j < len(grid[0]):
                        if grid[x + i][y + j] == 1:  # if neighbour is also land reduce permeter by 1
                            cur_pmtr -= 1
                            if not (x + i, y + j) in visited:
                                queue.append((x + i, y + j))
                perimeter += cur_pmtr  # after visiting all the neighbours add it to the tottal perimeter
        return perimeter
