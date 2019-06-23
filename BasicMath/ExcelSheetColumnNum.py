import string

class Solution:
    def titleToNumber(self, s: str) -> int:
        #Time - O(n) n = length of given string
        #Space - O(1) only need to store hasmap of aplhabets.
        alphalist = list(string.ascii_uppercase)
        #creating a hashmap for all alphabets as keys with their values.
        alphamap = {}
        for idx, elem in enumerate(alphalist):
            alphamap[elem] = idx + 1
        total = 0
        #Looping through the string adding it's value multiplied by it's positions value to the total.
        for i in range(len(s)):
            total += 26**(len(s) - 1 - i) * alphamap[s[i]]
        return total