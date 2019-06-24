class Solution:
    def reverseWords(self, s: str) -> str:
        # Solution without using indexing.
        # Time - O(n)
        # Space - O(n)
        if len(s) == 0:
            return s
        s_list = list(s) # Created a list of string to manipulate
        start = 0
        for i in range(len(s)): # loop through the list, if we we find any space, we will manipulate from start to space.
            if s_list[i] == " ":
                for j in range(0, (i - start) // 2):
                    s_list[start + j], s_list[i - j - 1] = s_list[i - j - 1], s_list[start + j]
                start = i + 1
        #Finally, Last word is left and handled seperately.
        for j in range(0, (i + 1 - start) // 2):
            s_list[start + j], s_list[i - j] = s_list[i - j], s_list[start + j]

        return "".join(s_list)

class Solution2:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        for word in s_list:
            word = word[::-1]
        return " ".join(s_list)
