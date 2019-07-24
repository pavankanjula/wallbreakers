class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #Time - O(n*2^n)
        #Space -O(n*2^n)
        output = [[]] #output list intiated
        for i in range(len(nums)): #Loop through the nums list and add it to all the sublists in the output and add all the newly created sublists to output
            temp = list(output)
            for j in range(len(temp)):
                sub = temp[j][:] + [nums[i]]
                output = output + [sub]
        return output