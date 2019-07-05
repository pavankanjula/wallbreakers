#Problem - https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        #Time - O(n) ; where n is length of string S.
        #Space - O(1); To store alphabets which string J contains. It can't be greater than 52(lowercase + uppercase).
        jewels = set() #stores the alphabets which string J contains.
        for each in J:
            jewels.add(each)
        count = 0
        for stone in S: #Iterate through the S and count if it is a jewel.
            if stone in jewels:
                count += 1
        return count