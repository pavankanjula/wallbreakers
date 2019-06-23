class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
	#Time - O(m*n) , m = row size, n = column size
	#Space - O(1)
        if len(A) == 0:
            return []
        row_len = len(A[0])
        col_len = len(A)
        #Loop through the rows and swap each element in a row with the element from last of the row.
        for row in A:
            half = row_len // 2
            i = 0
            while i < half:
                row[i], row[row_len - i -1] = row[row_len - i -1], row[i]
                i += 1
        # Replace 1 with 0 and 0 with 1 for all the elements in the matrix.
        for i in range(col_len):
            for j in range(row_len):
                if A[i][j] == 0:
                    A[i][j] = 1
                else:
                    A[i][j] = 0
        return A