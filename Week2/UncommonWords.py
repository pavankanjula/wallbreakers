class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        #Time - O(m + n) ; m = length of A, n = length of B
        #Space - O(m + n)
        hashA = {} #Stores all words in A with count
        for word in A.split():
            if word in hashA:
                hashA[word] += 1
            else:
                hashA[word] = 1
        hashB = {} #Stores all words in B with count
        for word in B.split():
            if word in hashB:
                hashB[word] += 1
            else:
                hashB[word] = 1
        uncommon = []
        for word in hashA.keys():#Checks each word if satisfies the rules to be uncommon and adds to uncommon list if satisfies.
            if hashA[word] == 1 and not word in hashB:
                uncommon.append(word)
        for word in hashB.keys():
            if hashB[word] == 1 and not word in hashA:
                uncommon.append(word)
        return uncommon