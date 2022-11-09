class Solution:
    def preorderTraversal(self, root):
        final = []
        
        def finder(node):
            if not node:
                return
            final.append(node.val)
            finder(node.left)
            finder(node.right)
            
        finder(root)
        return final
