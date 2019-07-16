class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Time - O(n) One loop through the entire list
        #Space - O(n) #To store the dp array
        if len(prices) == 0: #edge case handling
            return 0
        dp = [0 for i in range(len(prices))]
        max_profit = 0
        min_price = prices[0]
        for i in range(1,len(prices)):
            dp[i] = max(max_profit,  prices[i]-min_price)# storing max profit which can be made till current day
            min_price = min(min_price, prices[i])# updating minmum value
            max_profit = dp[i] #updating maximum profit
        return dp[-1]