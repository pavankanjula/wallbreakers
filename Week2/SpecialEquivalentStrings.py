class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        #Time - O(mn) ; m is avg length of word, n is length of list
        #Space - O(mn)
        #The logic here is two words are special-equivalent if letters in odd indices and even indices for both words are similar.
        hashset = set()
        for word in A:
            evens = word[::2] #letters in even indices
            odds = word[1::2] #letters in odd indices
            hashset.add((''.join(sorted(evens)), ''.join(sorted(odds))))
        return len(hashset)