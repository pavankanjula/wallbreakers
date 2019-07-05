import string


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # Time - O(m*n); m = avg length of word, n = length of list of words.
        # Space - O(m*n); m = avg length of word, n = length of list of words. To store in unique set.
        alphas = list(string.ascii_lowercase)  # List if lowercase alphabets.
        codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        hashmap = {}  # Hashmap to make the search in O(1).
        for i in range(len(alphas)):
            hashmap[alphas[i]] = codes[i]

        unique = set()
        for word in words:
            unique.add(self.morse(word, hashmap))  # adds only if not already present in the set.
        return len(unique)

    def morse(self, word, hashmap):  # returns the trasformed word.
        out = ""
        for letter in word:
            out = out + hashmap[letter]
        return out