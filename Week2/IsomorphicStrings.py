class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Time - O(n); n = string length
        # Space - O(n); To store in the hashmap
        hashmap = {}
        for i in range(len(s)):
            if s[i] in hashmap:  # if current element already appeared before in string s,
                # the corrsponding element should be presnt in string t. Otherwise they are not isomorphic
                if t[i] != hashmap[s[i]]:
                    return False
            else:
                if t[i] in hashmap and hashmap[t[i]] == t[i]:
                    return False
                hashmap[s[i]] = t[i]
        # Same logic as above but comparing s with t. just change the roles of both strings.
        hashmap = {}
        for i in range(len(t)):
            if t[i] in hashmap:
                if s[i] != hashmap[t[i]]:
                    return False
            else:
                if s[i] in hashmap and hashmap[s[i]] == s[i]:
                    return False
                hashmap[t[i]] = s[i]

        return True
