class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
	#Time - O(m*n), m = row size, n = column size of matrix.
	#Space - O(m*n)
        if len(A) == 0:
            return []
        rows = len(A)
        cols = len(A[0])
        transA = []
        #Created an empty matrix with no. of rows = no. columns of A
        for i in range(cols):
            transA.append([])
        #Converted all rows to columns.
        for i in range(cols):
            for j in range(rows):
                transA[i].append(A[j][i])
        #returned the transposed matrix
        return transA