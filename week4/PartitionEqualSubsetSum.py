class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        self.memo = {}  # To reduce recomputing, we store some computed values
        target = sum(nums)
        if target % 2 != 0:  # if sum of nums is odd, we cannot partition it into 2 equal subsets
            return False
        else:
            target = target // 2
        return self.DFS(nums, target, 0)

    def DFS(self, nums, target, idx):
        if (target, idx) in self.memo:
            return self.memo[(target, idx)]
        if target < 0:
            return False
        if target == 0:
            return True
        for i in range(idx, len(nums)):  # Generating combinations
            if self.DFS(nums, target - nums[i], i + 1):
                return True
        self.memo[(target, idx)] = False
        return False