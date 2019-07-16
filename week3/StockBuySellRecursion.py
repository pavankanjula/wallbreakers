class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Time - O(n)
        #Space - O(n) #recursion call stack
        self.max_profit = 0 #Tracks the maximum profit
        self.helper(prices, 0) #helper function used for recursion
        return self.max_profit
    def helper(self, price_list, max_price):
        if len(price_list) == 0:#if price list is coompletely traversed, return
            return
        cur_price = price_list.pop() #current day price
        profit = max_price - cur_price #profit if we consider current day price
        self.max_profit = max(profit, self.max_profit) #updating the max_profit
        next_pass = max(max_price, cur_price)
        self.helper(price_list, next_pass)