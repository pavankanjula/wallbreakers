class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        #Time - O(n); Loop through the list of candies.
        #Space - O(n); To store the list in a hashmap.
        hashmap = {}
        for candy in candies:
            if candy in hashmap:
                hashmap[candy] += 1
            else:
                hashmap[candy] = 1
        brother = 0
        sister = 0
        for candy in hashmap.keys(): #We will distribute one from each type to sister and the remaining all to brother.
            if hashmap[candy] == 1:
                sister += 1
            else:
                sister += 1
                brother += hashmap[candy] - 1
        if brother >= sister: #Now, if if brother has more or same as sister, then maximum possible types are distrbuted to sister.
            return sister
        else: #Otherwise we will give the half of extra from sister to brother.
            return sister - (sister - brother)//2