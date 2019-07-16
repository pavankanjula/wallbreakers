class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort() #sorts list g
        s.sort() #sorts list s
        cont_child = 0 #tracks number of content children.
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]: #if cookie j can be given to child i, add 1 to cont_child and go to next child and next cookie to compare
                cont_child += 1
                i += 1
                j += 1
            else: #if cookie is not enough for child i, we will try next cookie.
                j += 1
        return cont_child