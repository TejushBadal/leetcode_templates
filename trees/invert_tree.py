# PATTERN: Tree Recursion (DFS)

# Structure:
# 1. Base case: if not node: return None
# 2. Process current node (swap, check, etc.)
# 3. Recurse on children
# 4. Return node

# Key Insight: Either order works (process before/after recursion)
# - Process first = top-down
# - Process after = bottom-up

# Time: O(n) - visit all nodes
# Space: O(h) where h=height, worst case O(n) THE RECURSION CALL STACK TAKES UP SPACE!!

# MY Notes: keep the code clean, no redundant code. 

def dfs(root):

    if not root:
        return None
    
    root.left, root.right = root.right, root.left

    dfs(root.left)
    dfs(root.right)

    return root

#return dfs(root)