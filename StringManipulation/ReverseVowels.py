class Solution:
    def reverseVowels(self, s: str) -> str:
        #Time - O(n)
        #Space - O(n)
        #As strings are immutable, created a list with all characters in string to manipulate
        s_list = []
        for char in s:
            s_list.append(char)
        start = 0
        end = len(s_list) - 1
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        #while loop from start, if any vowel found, while loop from end to find vowel from back and replace both with one another.
        while start < end:
            if s_list[start] in vowels:
                while end > start and not s[end] in vowels:
                    end -= 1
                s_list[start], s_list[end] = s_list[end], s_list[start]
                end -= 1
            start += 1
        out = ""
        for elem in s_list:
            out = out + elem
        return out