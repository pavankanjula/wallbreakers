class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Time - O(n) where n is length of input array
        # Space - O(1)
        if len(strs) == 0:
            return ''
        common = strs[0]
        # Traverse through the list while updating the common prefix.
        for word in strs:
            common = self.precom(common, word)
            if common == '':
                return common
        return common

    def precom(self, word1, word2):
        # A helper function to compare two words and give common prefix
        child = ""
        i = 0
        while i < min(len(word1), len(word2)) and word1[i] == word2[i]:
            child = child + word1[i]
            i += 1
        return child