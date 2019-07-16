class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time - O(n)
        # Space - O(n)
        if self.stringSort(s) == self.stringSort(t):  # if sorted strings are equal, retuens true.
            return True
        return False

    def stringSort(self, string):  # Sorts given string in alphabetical order
        alphabetSize = 26
        counts = [0] * alphabetSize  # counts of occurances of each alphabet
        for c in string:
            counts[ord(c) - ord('a')] += 1
        new_str = []
        for i in range(len(counts)):  # each alphabet is multiplied by it's count and added to the list.
            new_str.append(chr(ord('a') + i) * counts[i])
        return "".join(new_str)  # finally return the string which is joined from a list.