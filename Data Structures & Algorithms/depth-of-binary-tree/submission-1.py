from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_height = 0
        q = deque()
        q.append((root, 1))

        while q:
            curr, depth = q.popleft()
            if curr:
                max_height = max(max_height, depth)
                q.append((curr.right, depth + 1))
                q.append((curr.left, depth + 1))
        return max_height


        