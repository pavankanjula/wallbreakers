class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #Time - O(logn)
        #space - O(1)
        pow2 = 1
        while pow2 < n:
            pow2 = pow2*2
        if pow2 == n:
            return True
        return False