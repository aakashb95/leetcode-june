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
# Optimal Approach: O(logn * logn)
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        node = root
        lh = rh = 0
        while node:
            lh += 1
            node = node.left

        node = root
        while node:
            rh += 1
            node = node.right

        if lh == rh:
            return 2 ** lh - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


# Recursive O(logn * logn)
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
