
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curr):
            if not curr:
                return 0
            
            l = dfs(curr.left)
            r = dfs(curr.right)
            
            if l is False or r is False or abs(l - r) > 1:
                return False
            r = dfs(curr.right)

            height = 1 + max(l,r)
            return height
        
        ans = dfs(root)

        if ans is not False:
            return True
        else:
            return False
