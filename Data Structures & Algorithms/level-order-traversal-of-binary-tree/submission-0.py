# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        dico = {}

        def dfs(tree, depth):
            nonlocal dico

            if not tree:
                return None
            
            if depth in dico:
                dico[depth].append(tree.val)
            else:
                dico[depth] = [tree.val]

            dfs(tree.left, depth + 1)
            dfs(tree.right, depth + 1)
        
        dfs(root, 0)

        for l in dico.values():
            res.append(l)

        return res