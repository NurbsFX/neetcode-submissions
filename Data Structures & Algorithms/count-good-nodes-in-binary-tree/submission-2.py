# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        if not root:
            return res
        
        def dfs(tree, maxValue):
            nonlocal res
            if not tree:
                return None
            
            if tree.val >= maxValue:
                res += 1
                maxValue = tree.val
            dfs(tree.left, maxValue)
            dfs(tree.right, maxValue)
        
        dfs(root, root.val)

        return res