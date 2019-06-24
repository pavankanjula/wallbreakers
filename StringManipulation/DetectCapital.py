import string


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Time - O(n)
        # Space - O(1)
        upper = list(string.ascii_uppercase)
        # Created a set of uppercase letters to optimize search time while checking if each character is uppercase or not.
        upperset = set()
        for elem in upper:
            upperset.add(elem)
        # caps will count the number of uppercase characters in the string.
        caps = 0
        for char in word:
            if char in upperset:
                caps += 1
        # For the given three cases, returns True if satisfied else False
        if caps == 0 or caps == len(word) or (word[0] in upperset and caps == 1):
            return True
        else:
            return False
