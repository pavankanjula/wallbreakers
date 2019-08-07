class Solution:
    def myPow(self, x: float, n: int) -> float:
        self.memo = {0: 1, 1: x}  # memoization to reduce re computations
        out = self.helper(x, abs(n))
        if n < 0:
            return 1 / out
        return out

    def helper(self, x, n):
        if n in self.memo:  # If already computed, just return it
            return self.memo[n]
        else:  # if not present in memo, split n in to halves and multiply
            out = self.helper(x, n // 2) * self.helper(x, n - (n // 2))
            self.memo[n] = out  # Add the computed value to memo.
            return out