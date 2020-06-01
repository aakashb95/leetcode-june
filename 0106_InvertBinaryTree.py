# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert(root):
            if root == None:
                return
            else:
                # temp = root
                root.left, root.right = root.right, root.left
                invert(root.right)
                invert(root.left)

            #                 temp = root.left
            #                 root.left = root.right
            #                 root.right = temp
            return root

        return invert(root)


#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9

