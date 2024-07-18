# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        # maps TreeNodes to neighbors
        graph = defaultdict(set)
        def createGraph(parent, leftChild, rightChild):
            if not parent:
                return
            if leftChild: 
                graph[parent].add(leftChild)
                graph[leftChild].add(parent)
                createGraph(leftChild, leftChild.left, leftChild.right)
            if rightChild:
                graph[parent].add(rightChild)
                graph[rightChild].add(parent)
                createGraph(rightChild, rightChild.left, rightChild.right)

        createGraph(root, root.left, root.right)
        
        def isLeaf(node):
            return not (node.left or node.right)

        def bfs(node):
            currDistance = 0
            queue = deque()
            queue.append(node)
            visited = set()
            res = 0
            for _ in range(distance):
                for _ in range(len(queue)):
                    currNode = queue.popleft()
                    if currNode in visited:
                        continue
                    visited.add(currNode)
                    for neighborNode in graph[currNode]:
                        if neighborNode in visited:
                            continue
                        if isLeaf(neighborNode):
                            res += 1
                        else:
                            queue.append(neighborNode)
            return res

        goodLeafNodePairs = 0
        for node in graph:
            if isLeaf(node):
                goodLeafNodePairs += bfs(node)

        return goodLeafNodePairs // 2