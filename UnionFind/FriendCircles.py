class Solution:
    def __init__(self):
        self._circles = 0

    def findCircleNum(self, M: List[List[int]]) -> int:
        # Time - O(n**2)
        # Space - O(n)
        # Using Union-Find data structure
        self._circles = len(M)
        parents = [0] * len(M)  # Initiate an array of all guys where each guy is a seperate friend circle.
        ranks = [0] * len(M)
        for i in range(len(M)):
            parents[i] = i
        for i in range(len(M)):
            for j in range(i, len(M)):  # For each relation between two guys in the matrix
                if i != j and M[i][j] == 1:  # if 1, we will do union operation for the guys.
                    self.union(i, j, parents, ranks)
        return self._circles

    def find(self, p, parents):  # method to find the root of the friend circle which the guy belongs to.
        while p != parents[p]:
            parents[p] = parents[parents[p]]
            p = parents[p]
        return p

    def union(self, p, q, parents, ranks):  # Method to combine two friends into a single group.
        rootP = self.find(p, parents)
        rootQ = self.find(q, parents)
        if rootP == rootQ:  # If both are in same circle, no need to do anything.
            return
        if ranks[rootP] > ranks[
            rootQ]:  # Based on rank we will join the guy into a circle with highrank(more number of guys)
            parents[rootQ] = rootP
        elif ranks[rootQ] > ranks[rootP]:
            parents[rootP] = rootQ
        else:
            parents[rootQ] = rootP  # If both has same rank, arbitrarily join one guy to other group.
            ranks[rootP] += 1  # Increase the rank by 1
        self._circles -= 1  # as 1 guy joins to a circle, we will reduce one from number of circles count.
