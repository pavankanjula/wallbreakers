class Solution:
    def findOrder(self, numCourses, prerequisites):
        #Time - O(V+E)
        #Space - O(V+E)
    # Converting the given data into adjacent list Graph structure.
        adj_list = {}
        for i in range(numCourses):
            adj_list[i] = []
        for each in prerequisites:
            adj_list[each[1]].append(each[0])

        output = [] #stores the courses while doing DFS.
        visited = set()
        for key in adj_list.keys(): #Iterate through all the nodes
            if not key in visited: #If node was not visited before, apply DFS to find if there is cycle.
                path = set() #To track the path for each node while doing DFS
                if self.DFS(key, adj_list, output, visited, path):
                    return []
        return output[::-1]

    def DFS(self, cur_node, graph, out, visited, cur_path):
        #General DFS Cycle finding parallelly adding the courses to output array in reverse.
        #Does this called as Back tracking? just wanna know
        visited.add(cur_node)
        cur_path.add(cur_node)
        for nbr in graph[cur_node]:
            if nbr in cur_path:
                return True
            if not nbr in visited:
                if self.DFS(nbr, graph, out, visited, cur_path):
                    return True
        cur_path.remove(cur_node)
        out.append(cur_node)
        return False