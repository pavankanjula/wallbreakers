class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Time - O(n* n!)
        # Space - O(n* n!)
        # Basic idea here is to put the new element in all the places of the previous permutations and generate the new permutations.
        if len(nums) == 0:
            return [[]]
        output = [[nums[0]]]
        for i in range(1, len(nums)):
            temp = output[:]
            output = []
            for j in range(len(temp)):
                sub = temp[j]
                for h in range(len(sub) + 1):
                    sub_temp = sub[:h] + [nums[i]] + sub[h:]
                    output = output + [sub_temp]
        return output


"""
EXPLAINATION WITH EXAMPLE
nums - [1,2,3]
generator initiation - [[1]]
iteration 1 
    [[2,1], [1,2]]
iteration 2
    [[3,2,1],[2,3,1],[2,1,3],[3,1,2],[1,3,2],[1,2,3]]
"""