# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # DFS
        count = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                stack.extend([node.left, node.right])
                count += 1

        return count


# TODO: #2 Add optimal approach here

