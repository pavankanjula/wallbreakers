class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.output = []  # To store the combinations with the target sum
        self.DFS(candidates, target, [])  # recursive DFS function
        return self.output

    def DFS(self, nums, req, cur):
        if req < 0:  # if required number gets below 0, we cannot find it anymore and return
            return
        if req == 0:  # if required number is 0 means, we achieved the target sum and we can append this sublist to output.
            self.output.append(cur)
            return
        for i in range(len(nums)):  # Check if adding any of the number satisfies the condition in a recursive way.
            arg = cur[:] + [nums[i]]
            self.DFS(nums[i:], req - nums[i], arg)
