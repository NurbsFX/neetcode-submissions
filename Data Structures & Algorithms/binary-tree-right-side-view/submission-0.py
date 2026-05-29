# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(tree, depth):
            if not tree:
                return None
            if depth == len(res):
                res.append(tree.val)
            dfs(tree.right, depth + 1)
            dfs(tree.left, depth+1)
        
        dfs(root, 0)
        return res