from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #Time - O(m*n)
        #Space - O(m*n)
        if len(grid) == 0:
            return 0
        nrow = len(grid)
        ncol = len(grid[0])
        #visited set to track the elements we visited.
        visited = set()
        islands = 0 # This is where we count the number of islands.
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        for i in range(nrow):
            for j in range(ncol): #Loop through all positions in th grid.
                if grid[i][j] == '1' and not (i,j) in visited:
                    queue = deque() # intiating a queue
                    queue.append((i,j))
                    while queue:
                        x,y = queue.popleft()
                        if (x,y) in visited:
                            continue
                        visited.add((x,y))
                        for a,b in directions: #checking the neighbours of the current position.
                            if not (x+a < 0 or x+a >= nrow or y+b < 0 or y+b >= ncol): #checking if neighbour is within the grid limits.
                                if grid[x+a][y+b] == '1':
                                    queue.append((x+a, y+b)) #adding to queue
                    islands += 1 #Since we have grouped an island, we will increase the count by 1.
        return islands