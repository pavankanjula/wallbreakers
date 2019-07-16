class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #Time - O(nlogn) #For sorting the list.
        #Space - O(n) #python uses mergesort which takes O(n) space
        if len(intervals) == 0:
            return []
        intervals.sort() #Sorts the list on first element of sublists
        out = [intervals[0]] #Output list
        for i in range(1, len(intervals)):
            if intervals[i][0] <= out[-1][1]: #if current interval start is less than previous merged interval endtime, merge it to the previous merged interval.
                out[-1][1] = max(intervals[i][1],out[-1][1])
            else: #otherwise just add it as it is
                out.append(intervals[i])
        return out