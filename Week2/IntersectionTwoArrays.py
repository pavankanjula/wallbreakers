class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Time - O(m + n) ; m, n = length of arrays
        #Space - O(m + n)
        set1 = set() #Created a set for nums1 which contains only unique values
        for num in nums1:
            set1.add(num)
        set2 = set() #Created a set for nums2
        for num in nums2:
            set2.add(num)
        output = []
        for num in set1: #loop through a set and if we find it in the other set, we will append it to output
            if num in set2:
                output.append(num)
        return output