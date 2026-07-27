class Node:
    def __init__(self):
        self.end = False
        self.next = {}
        self.val = ''

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        temp = self.root
        for c in list(word):
            if c in temp.next.keys():
                temp = temp.next[c]
            else:
                temp.next[c] = Node()
                temp = temp.next[c]
        temp.end = True

    def search(self, word: str) -> bool:
        wordlist = list(word)
        def searchFromIndex(root: Node, index: int) -> bool:
            if index >= len(wordlist):
                return root.end
            temp = root
            for i in range(index, len(wordlist)):
                c = wordlist[i]
                if c == '.':
                    foundMatch = False
                    for key in temp.next.keys():
                        foundMatch = foundMatch or searchFromIndex(temp.next[key], i + 1)
                    return foundMatch

                if c in temp.next.keys():
                    temp = temp.next[c]
                else:
                    return False
            return temp.end

        return searchFromIndex(self.root, 0)

        
