class Solution:
    def binaryGap(self, N: int) -> int:
        # Time - O(logn)
        # Space - O(1)
        longest = float('-inf') #A variable to update the longest distance everytime we find a 1.
        i = 2
        while i < len(bin(N)) and bin(N)[i] != '1': #Finding where the first 1 is
            i += 1
        count = 0
        for num in bin(N)[i + 1:]:
            if num == '0': #count it
                count += 1
            if num == '1': #count, update longest and set count to 0 again to count the next streak of 0's
                count += 1
                longest = max(count, longest)
                count = 0

        return max(longest, 0)