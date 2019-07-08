class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        #Time - O(logN) ; N = length of array A
        #Space - O(1)
        left = 0
        right = len(A) - 1
        #According to the given conditions
        while left <= right:
            mid = (left + right)//2
            print(mid)
            if mid == 0 or mid == len(A)-1:# we reached either ends without finding any peak so this should be the peak.
                return mid
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:# if this is satisfied we found the peak
                return mid
            elif A[mid] < A[mid+1]: # this means we can neglect all the left side array
                left = mid + 1
            else: #we can neglect all the right side array.
                right = mid - 1