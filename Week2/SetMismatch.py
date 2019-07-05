import collections
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        #Time - O(n)
        #Space - O(n)
        multiset = collections.Counter(nums) #Stores the list elements with no. of occurances.
        miss = -1 #To assign the missing element while doing for loop.
        twice = -1 # To assign the element which occured twice.
        for i in range(1, len(nums)+1):
            if multiset[i] == 2:
                twice = i
            if not i in multiset:
                miss = i
        return [twice, miss]