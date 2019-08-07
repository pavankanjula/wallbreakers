class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #Time - O(n)
        #Space - O(1)
        if len(p) > len(s) :
            return []
        output = []
        hash_p = collections.Counter(p)
        #Take a substring of s with length of p.
        hash_s = collections.Counter(s[:len(p)])
        #Compute counter hashmaps for both and run a for loop making substring as a sliding window.
        #whenever their counters hashmaps are same, add the start index to output.
        if hash_p == hash_s:
            output.append(0)
        for i in range(len(p), len(s)):
            if hash_s[s[i - len(p)]] > 1:
                hash_s[s[i - len(p)]] -= 1
            else:
                del(hash_s[s[i - len(p)]])
            if s[i] in hash_s:
                hash_s[s[i]] += 1
            else:
                hash_s[s[i]] = 1
            if hash_p == hash_s:
                output.append(i - len(p) + 1)
        return output