import collections
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ctr = collections.Counter(s)
        for char in  t:
            if not char in ctr or ctr[char] == 0:
                return char
            else:
                ctr[char] -= 1
        return "�"