class Solution:
    def rob(self, nums: List[int]) -> int:
        # Time - O(n)
        # Space - O(n)
        # Two cases to consider either include first house or not
        if len(nums) == 0:
            return 0
        if len(nums) <= 3:
            return max(nums)
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))  # taking max value of two cases.

    def helper(self, houses):  # return max amount which can rob in a straight list.
        if len(houses) == 0:
            return 0
        if len(houses) <= 2:
            return max(houses)
        dp = [0 for i in range(len(houses))]
        dp[0], dp[1] = houses[0], max(houses[0], houses[1])
        for i in range(2, len(houses)):
            dp[i] = max(dp[i - 2] + houses[i], dp[i - 1])  # updating current value based on the previous values.
        return dp[-1]