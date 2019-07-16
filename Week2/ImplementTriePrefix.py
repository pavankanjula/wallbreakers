class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()  # Initialize root as a node with empty children dictionary.

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curNode = self.root
        for char in word:  # Loop trough the given word.
            if char not in curNode.children:  # If we don't find a character, we will put one.
                curNode.children[char] = Node()
            curNode = curNode.children[char]
        curNode.isWord = True  # Finally at end of the word, we will make isWord to True to make it as a word.

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        # Traverse through the Trie from root. If we don't find a character, return False.
        curNode = self.root
        for char in word:
            if char in curNode.children:
                curNode = curNode.children[char]
            else:
                return False
        # Finally if we reach the end of word, we will retuen True if isWord was set to True otherwise False
        return curNode.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        # Only difference between search method and this is, here we return return True if we reach the end of word regardless of the isWord property.
        curNode = self.root
        for char in prefix:
            if char in curNode.children:
                curNode = curNode.children[char]
            else:
                return False
        return True