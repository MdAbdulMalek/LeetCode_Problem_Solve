class Solution:
    def inorderTraversal(self, root):
        final = []       
        def finder(node):
            if not node:
                return
            finder(node.left)
            final.append(node.val)
            finder(node.right)       
        finder(root)
        return final  
ob1 = Solution()
print(ob1.inorderTraversal([1,null,2,3]))
