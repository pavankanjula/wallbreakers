class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #Time - O(n) ; n is length of s
        #Space - O(1) #as the number of alphabets are 26
        if len(p) > len(s) : #if length of s is less than p, return empty list.
            return []
        output = []
        hash_p = collections.Counter(p) # counter hashmap of characters of p
        hash_s = collections.Counter(s[:len(p)]) #counter hashmap of characters of s till length of p.
        #From here, we use sliding window technique.
        if hash_p == hash_s:
            output.append(0)
        for i in range(len(p), len(s)):
            #remove the first element and add the next element in s.
            if hash_s[s[i - len(p)]] > 1:
                hash_s[s[i - len(p)]] -= 1
            else:
                del(hash_s[s[i - len(p)]])
            if s[i] in hash_s:
                hash_s[s[i]] += 1
            else:
                hash_s[s[i]] = 1
            if hash_p == hash_s: #compare if both hashmaps are same, and append the start index if True
                output.append(i - len(p) + 1)
        return output