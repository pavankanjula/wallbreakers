class Solution:
    #Time complexity - O(n)
    #Space complexity - O(1)
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        #current pointer to travel the list from start to end
        current = 0
        #prev pointer to track the index with even number from where we swapped with an odd number previously.
        prev = 0
        while current < len(A) and prev < len(A):
            #if the current elemnt is odd, we will swap it with next even element in the array
            if A[current] % 2 != 0:
                #prev pointer should be right to the current odd element.
                prev = max(current,prev)
                #Prev pointer travelling to the next available even number in the array
                while A[prev] % 2 != 0:
                    prev += 1
                    if prev >= len(A):
                        #if prev reach the end, that means no even numbers left and we can return the array.
                        return A
                A[current],A[prev] = A[prev],A[current]
            current += 1
        return A