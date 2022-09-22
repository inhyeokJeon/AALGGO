import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, index= 0, val = 0, left = None, right = None):
        self.index = index
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = Node()

    def insert(self, index, val):
        self.root = self._insert(self.root, index, val)
        return self.root is not None

    def _insert(self, node, index, val):
        if node is None:
            return Node(index, val)
        if val < node.val:
            node.left = self._insert(node.left, index, val)
        else:
            node.right = self._insert(node.right, index, val)

        return node

    def preorder(self) -> list:
        node = self.root
        result = []
        def preorder(nd):
            if nd:
                result.append(nd.index)
                if nd.left:
                    preorder(nd.left)
                if nd.right:
                    preorder(nd.right)
        preorder(node)
        result.pop(0)
        return result

    def postorder(self) -> list:
        node = self.root
        result = []
        def preorder(nd):
            if nd:
                if nd.left:
                    preorder(nd.left)
                if nd.right:
                    preorder(nd.right)
                result.append(nd.index)
        preorder(node)
        result.pop()
        return result

def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i)
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))
    bt = Tree()
    for val, _, index in nodeinfo:
        bt.insert(index + 1, val)

    return [bt.preorder(), bt.postorder()]


nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
# ans = [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
print(solution(nodeinfo))
