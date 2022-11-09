class Solution:
    def postorderTraversal(self, root):
        final = []
        def finder(node):
            if not node:
                return
            finder(node.left)
            finder(node.right)
            final.append(node.val)
        finder(root)
        return final
