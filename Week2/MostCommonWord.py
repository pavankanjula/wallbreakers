class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #Time - O(n)
        #Space - O(n)
        paragraph = paragraph.translate(str.maketrans('', '', string.punctuation)).lower()#String preprocessing
        parastrip = paragraph.split() #Split into list of words.
        ban_set = set(banned) #set of banned words.
        multiset = {} #multiset for words which are not in banned set.
        for word in parastrip:
            if not word in ban_set:
                if word in multiset:
                    multiset[word] += 1
                else:
                    multiset[word] = 1
        highfreq = max(multiset.values()) #highest frequency
        for key,value in multiset.items():
            if value == highfreq: #return the key where value is highest.
                return key