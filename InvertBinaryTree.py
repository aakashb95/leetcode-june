# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Recursion
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

#BFS:

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = collections.deque([(root)])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root

#DFS:

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.left, node.right])
        return root
