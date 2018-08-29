"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

"""

class TreeNode(object):
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root==None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        p=root
        if p.lelft==None:
            return
        p=p.left
        while p.right:
            p=p.right
        p.right=root.right
        root.right=root.left
        root.left=None
        
            
            
