class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #Time - O(n)
        #Space - O(1)
        # Loop through the list and replace every character with the character at the same distance from backside.
        for i in range(len(s)//2) :
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]