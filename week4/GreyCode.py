class Solution:
    def grayCode(self, n: int) -> List[int]:
        #Time - O(2^n)
        #Space - O(2^n)
        if n == 0:
            return [0]
        out = ['0','1']
        for i in range(1, n):
            temp = []
            for i in range(len(out)):
                temp.append('0' + out[i])
            for j in range(len(out)-1, -1, -1):
                temp.append('1' + out[j])
            out = temp
        for i  in range(len(out)):
            out[i] = int(out[i],2)
        return out