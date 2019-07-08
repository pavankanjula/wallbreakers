class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Time - O(logN) ; N = length of given array
        #Space - O(1)
        left = 0
        right = len(nums) - 1
        #AS the array is in increasing order, if we find the middle number greater than target, we can just skip checking all the numbers right to that and if if less than target, we can skip checking all the number left to that.
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: #if found return index
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1