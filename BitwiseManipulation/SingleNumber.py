class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #Time - O(n)
        #Space - O(1)
        #XOR follows the cummulative A xor B = B xor A  and the associative A xor (B xor C) = (A xor B) xor C.
        # A xor A = 0
        #if we implment XOR through the loop, all the repeated numbers become 0 and one single number will be left.
        out = 0
        for num in nums:
            out ^= num
        return out