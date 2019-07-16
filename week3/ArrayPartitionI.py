class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        #Time - O(nlogn) #To sort the array
        #Space - O(n) #as sort() method is built using mergesort technique.
        nums.sort()
        return sum(nums[::2]) #after sorting, as we need to maximize the sum of pairs, we can consider alternate element from start to end.