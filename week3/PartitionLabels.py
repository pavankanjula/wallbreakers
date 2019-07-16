class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        #Time - O(n) ; n is length of S
        #Space - O(1) ; As the hashmap takes constanct space.
        if len(S) == 0:
            return []
        output = []
        hashmap = {}
        for idx, char in enumerate(S):
            hashmap[char] = idx #Stores all the charcaters with values of indices when last present.
        start = 0 #To track start index of partitioned substring
        i = 0 #starts from 0 index
        j = hashmap[S[0]] #end of current substring.
        while i < len(S) and j < len(S):
            if i == j: #if both meet, we can partition it
                output.append(i - start + 1)
                start = i+1
            i += 1
            if i < len(S):
                j = max(j,hashmap[S[i]]) #updates end of the substring with latest end index.
        return output