class Solution:
    def findComplement(self, num: int) -> int:
        #Time - O(logn)
        #Space - O(1)
        #XOR operation with all '1's will convert 1 -> 0  and 0 -> 1.
        if num == 0:
            return 1
        power = 0
        while 2**power <= num: #Find the number with all '1's with same length of given numer binary form.
            power += 1
        return num^(2**power - 1) #XOR operation