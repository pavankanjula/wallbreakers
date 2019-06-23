class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Time - O(n)
        #Space - O(1)
        seen = {}
        #Creating a hashmap of letters and count for one string
        for char in s:
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1
        #Validate the other string with the hashmap.
        for char in t:
            if not char in seen or seen[char] == 0:
                return False
            else:
                seen[char] -= 1
        if sum(seen.values()) > 0:
            return False
        return True
