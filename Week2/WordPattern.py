class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        # Time - O(n); n = length of pattern
        # Space - O(n) #To store the key value pairs in hashmap
        if len(pattern) != len(str.split()):
            return False
        hashmap = {}
        string = str.split()
        for i in range(len(pattern)):
            if pattern[i] in hashmap:  # if current character already appeared before in string s,
                # the corrsponding word should be presnt in sentence str. Otherwise they mismatch the pattern
                if hashmap[pattern[i]] != string[i]:
                    return False
            else:
                if string[
                    i] in hashmap.values():  # if current character not present before, the current corresponding word should not be present before.
                    return False
                hashmap[pattern[i]] = string[i]
        return True
