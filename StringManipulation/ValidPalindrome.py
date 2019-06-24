class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Time - O(n)
        #Space - O(n)
        dup = ""
        #Cleaning the given string to keep only alphabets and numeric characters.
        for char in s:
            if char.isalnum():
                dup = dup + char.lower()
        #Check if every character is equal to the corresponding character from backside.
        for i in range(len(dup)//2):
            if dup[i] != dup[len(dup) - 1 - i]:
                return False
        return True