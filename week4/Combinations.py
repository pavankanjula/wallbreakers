class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Time - n!/(k-1)!(n-k)!
        # Space - n!/(k-1)!(n-k)!
        output = [[i] for i in range(1, n - k + 2)]
        for i in range(k - 1):  
            temp = output[:]
            output = []
            for j in range(len(temp)):
                for h in range(temp[j][-1] + 1, n - k + i + 3):
                    sub = temp[j][:] + [h]
                    print(sub)
                    output = output + [sub]
        return output


"""
EXPLAINATION WITH EXAMPLE 
lets take n = 5, k = 4
Final result should be [[1,2,3,4],[1,2,3,5],[1,2,4,5],[1,3,4,5],[2,3,4,5]]
output list intiated at first will be [1,2]
k-1 iterations --> total 3 iterations as we already intiated output with first elements of each combination.
1st iteration -->
     temp copies output and output get empty to take next combined sublists.
     output - [[1,2],[1,3],[2,3]]
2nd iter -->
     output - [[1,2,3],[1,2,4],[1,3,4],[2,3,4]]
3rd iter -->
     output - [[1,2,3,4],[1,2,3,5],[1,2,4,5],[1,3,4,5],[2,3,4,5]]
So each time every sublist takes different possible combinations from the remaining elememts and creates a new list of sublists.

"""