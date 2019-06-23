class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Time - O(n)
        #Space - O(n)
        #A hashmap to to store the previously seen elements
        seen_map = {}
        for index, num in enumerate(nums):
            #if the matching number is in hashmap, we return indices. Otherwise add it to the hashmap
            if target - num in seen_map:
                return sorted([index, seen_map[target - num]])
            else:
                seen_map[num] = index