class PrefixTree:

    def __init__(self):
        self.root = [None for _ in range(27)]

    def insert(self, word: str) -> None:
        temp = self.root
        for c in list(word):
            index = ord(c) - ord('a')
            if not temp[index]:
                temp[index] = [None for _ in range(27)]
            temp = temp[index]
        temp[26] = True


    def search(self, word: str) -> bool:
        temp = self.root
        for c in list(word):
            index = ord(c) - ord('a')
            if not temp[index]:
                return False
            temp = temp[index]
        return temp[26] == True


    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for c in list(prefix):
            index = ord(c) - ord('a')
            if not temp[index]:
                return False
            temp = temp[index]
        return True
        
        