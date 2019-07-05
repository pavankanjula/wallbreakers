import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        #Time - O(n)
        #Space - O(n)
        if len(s) == 0:
            return -1
        hashmap = collections.Counter(s) #a dictionary with count of all characters
        reqset = set() #stores all unique characters
        for key in hashmap:
            if hashmap[key] == 1:
                reqset.add(key)
        if len(reqset) == 0:
            return -1
        for i in range(len(s)): #While looping, we will return the first ever character which is in reqset
            if s[i] in reqset:
                return i
        return -1