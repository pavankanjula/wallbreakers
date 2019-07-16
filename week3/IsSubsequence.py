class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #Time - O(m + n) ; m is length of s and n is length of t
        #Space - O(1)
        i = 0 #counter for index in string s
        j = 0 #counter for index in string t
        while i < len(s) and j < len(t):
            if s[i] == t[j]: #if char from s matches with char in t, move to next element in both strings.
                print((i,j))
                i += 1
                j += 1
            else: # if not matches, try comparing the next character in t.
                j += 1
        #Finally if all chars of s are matched with chars of t, return True
        if i < len(s):
            return False
        return True