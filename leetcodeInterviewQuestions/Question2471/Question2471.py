class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        store,res = [root],0
        while store:
            temp,cur,nex = [],{},[]
            for i,node in enumerate(store):
                temp.append(node.val)
                cur[node.val] = i
                if node.left:
                    nex.append(node.left)
                if node.right:
                    nex.append(node.right)
            temp1 = temp.copy()
            temp.sort()
            for i in range(len(store)):
                node = temp[i]
                while temp[i]!=temp1[i]: # Keep swapping until settled
                    pos = cur[temp[i]]
                    temp[i],temp[pos] = temp[pos],temp[i]
                    res+=1
            store = nex # BFS
        return res