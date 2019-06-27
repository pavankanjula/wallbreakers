class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        #Time - O(length(max(x,y)))
        #Space - O(n)

        dist = 0
        for bit in bin(x^y): # XOR gives 1's where there are different digits in both binary numbers
            if bit == '1':
                dist += 1 #count all the 1's
        return dist