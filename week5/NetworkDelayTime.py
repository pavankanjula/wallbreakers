import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # Time - O(len(times)*logN)
        # Space - O(E+V)
        adj_list = {}  # Creates a graph data structure
        for i in range(1, N + 1):
            adj_list[i] = []
        for each in times:
            adj_list[each[0]].append((each[1], each[2]))

        memo = {}  # To hold minimum time from node K.
        for i in range(1, N + 1):
            memo[i] = float('inf')
        memo[K] = 0
        visited = set()
        pq = []  # Min heap to release the next node with minimum time
        heapq.heappush(pq, (0, K))
        while pq:
            minTime, idx = heapq.heappop(pq)
            visited.add(idx)
            for nbr, time in adj_list[
                idx]:  # For each neighbour, we calculate time from current node and updates if it is less than before.
                if nbr in visited:
                    continue
                newTime = minTime + time
                if newTime < memo[nbr]:
                    memo[nbr] = newTime
                    heapq.heappush(pq, (newTime, nbr))
        # Finally, if we have node with infinity time, that means we cannot reach that node in the graph and return -1 else, return maximum of times to reach each node
        out = max(memo.values())
        if out == float('inf'):
            return -1
        else:
            return out