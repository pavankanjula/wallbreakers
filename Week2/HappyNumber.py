class Solution:
    def isHappy(self, n: int) -> bool:
        # Time - O(1)
        # Space - O(1)

        seen = set()  # To track the numbers already came before. Helps to check the loop
        seen.add(n)
        while n != 1:
            n = self._score(n)
            if n in seen:  # Identifies Loop
                return False
            else:
                seen.add(n)
        return True

    def _score(self, n):  # calucullates the sum of the squares of individual digits of given number.
        score = 0
        while n > 0:
            out = n % 10
            score = score + out ** 2
            n = n // 10
        return score