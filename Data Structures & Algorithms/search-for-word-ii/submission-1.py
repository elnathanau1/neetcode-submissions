class Node: 
    def __init__(self):
        self.next = [None] * 26
        self.end = False
        self.word = ""
        self.prev = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def createTrie() -> Node:
            rootNode = Node()
            for word in words:
                temp = rootNode
                prev = None
                for c in list(word):
                    index = ord(c) - ord('a')
                    if not temp.next[index]:
                        temp.next[index] = Node()
                        prev = temp
                        temp = temp.next[index]
                        temp.prev = prev
                    else:
                        temp = temp.next[index]
                    
                temp.end = True
                temp.word = word

            return rootNode

        
        def getIndex(char: str) -> int:
            return ord(char) - ord('a')


        rootNode = createTrie()
        
        node = rootNode
        foundSet = set()
        seen = set()
        def dfs(i: int, j: int, node: Node):
            index = getIndex(board[i][j])
            if not node.next[index]:
                return
            node = node.next[index]
            
            seen.add((i,j))
            if node.end:
                foundSet.add(node.word)
            
            for nextI, nextJ in [(i-1, j), (i+1, j), (i, j-1), (i,j+1)]:
                if nextI >= 0 and nextI < len(board) and nextJ >= 0 and nextJ < len(board[0]) and (nextI, nextJ) not in seen:
                    dfs(nextI, nextJ, node)
            seen.remove((i,j))

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j, rootNode)           
        

        return list(foundSet)