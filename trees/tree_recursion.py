# ===============================================
# PATTERN: Tree DFS Recursion (Return Values)
# ===============================================

# CORE STRUCTURE:
# --------------
# def treeFunction(self, root):
#     # 1. Base case - handle null/empty
#     if not root:
#         return [base_value]  # 0, None, True, etc.
    
#     # 2. Recursive case - process children FIRST
#     left_result = self.treeFunction(root.left)
#     right_result = self.treeFunction(root.right)
    
#     # 3. Combine results + process current node
#     current_result = [combine left_result and right_result]
    
#     # 4. Return the answer
#     return current_result

# KEY PRINCIPLES:
# --------------
# ✅ Make the METHOD itself recursive (no nested dfs function)
# ✅ Return values carry the answer (no extra variables)
# ✅ Base case: if not root: return [something]
# ✅ Process children, then combine their results

# COMPLEXITY:
# -----------
# Time: O(n) - visit each node once
# Space: O(h) where h = height
#   - Balanced tree: O(log n)
#   - Skewed tree: O(n)
#   - Space = recursion call stack depth


# EXAMPLES:
# ---------
# 1. Max Depth:
#    - Base: if not root: return 0
#    - Recursive: return 1 + max(left_depth, right_depth)

# 2. Invert Tree:
#    - Base: if not root: return None
#    - Recursive: swap children, recurse both, return root

# 3. Same Tree (Compare Two Trees):
#    - Base cases:
#      * Both None → True
#      * One None → False  
#      * Values differ → False
#    - Recursive: return left_same AND right_same
#    - KEY: Take TWO nodes as parameters, compare simultaneously

# 4. Subtree of Another Tree (Combining Patterns):
#    - Helper: Reuse isSameTree(p, q)
#    - Main recursion:
#      * Base: if not root → False
#      * Check current: same_tree(root, subRoot) → True
#      * Recurse: isSubtree(left) OR isSubtree(right)
#    - KEY: Use OR logic (any match works)
#    - Complexity: O(n×m) time - nested operation!

# 5. Lowest Common Ancestor of BST:
#    - Use BST property: left < root < right
#    - Both smaller → go left
#    - Both larger → go right
#    - Split (or equal) → return current
#    - Iterative: O(log n) time, O(1) space ✅
#    - Recursive: O(log n) time, O(h) space
#    - KEY: Only ONE path, not all nodes!
#    - MY MISTAKE: Said O(n) but it's O(h) - only one path!

# 6. Binary Tree Level Order Traversal (BFS):
#    - Use deque for queue (O(1) popleft)
#    - KEY TRICK: level_size = len(queue) before for loop
#    - Process exactly level_size nodes per level
#    - Add children during processing (queue grows)
#    - Time: O(n), Space: O(n) - queue holds nodes
#    - Date: Oct 31, took 5 min with template (NORMAL!)
#    - NOTE: This is THE pattern for level-order problems

# COMMON MISTAKES (MY MISTAKES):
# ------------------------------
# ❌ Using nested dfs() function (unnecessary)
# ❌ Using extra variables to track state (nonlocal, etc.)
# ❌ Not returning the computed value directly
# ❌ Forgetting base case → infinite recursion
# ❌ Checking "if not root.left and not root.right" instead of "if not root"


# WHEN TO USE:
# ------------
# ✅ Need a single value from entire tree (depth, sum, count)
# ✅ Need to check a property (valid BST, balanced, etc.)
# ✅ Need to transform tree (invert, copy, etc.)
# ✅ Problem has obvious recursive relation


# WHEN NOT TO USE (use BFS instead):
# ----------------------------------
# ❌ Need level-by-level processing
# ❌ Need shortest path
# ❌ Explicitly asked for level-order


# MY BREAKTHROUGH MOMENT:
# ----------------------
# Problem: Max Depth of Binary Tree
# Date: [oct 31]
# Time Taken: [15mins]
# Key Learning: Return values carry the answer - no need for extra variables or nested functions


# TEMPLATE CODE (copy-paste starting point):
# ------------------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))

def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # Base case 1: Both empty → identical
    if not p and not q:
        return True
    
    # Base case 2: One empty, one not → different
    if not p or not q:
        return False
    
    # Base case 3: Different values → different
    if p.val != q.val:
        return False
    
    # Recursive: Check both subtrees
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# KEY INSIGHT:
# -----------
# ✅ Function takes TWO tree nodes (not one!)
# ✅ Compare at each level, don't store anything
# ✅ Return True/False directly (no tracking variables)
# ✅ Multiple base cases needed (both None, one None, values differ)

# ===============================================
# 7. Validate Binary Search Tree (BST Validation)
# ===============================================

# PROBLEM: Check if a binary tree is a valid BST

# KEY TRAP: 
# ---------
# ❌ WRONG: Just checking node.left < node < node.right
# ✅ RIGHT: ALL left subtree nodes < node < ALL right subtree nodes

# Example trap case:
#      5
#     / \
#    1   6
#       / \
#      3   7  ← Node 3 is invalid! (3 < 5 but in right subtree)
# APPROACH 1: Inorder Traversal (What I Used)
# --------------------------------------------
# Insight: Inorder of valid BST = strictly increasing sequence

def isValidBST(self, root):
    prev = None
    
    def inorder(node):
        nonlocal prev
        if not node:
            return True
        
        # Check left subtree
        if not inorder(node.left):
            return False
        
        # Check current node vs previous
        if prev and node.val <= prev.val:
            return False
        prev = node  # ← CRITICAL: Update prev!
        
        # Check right subtree
        return inorder(node.right)
    
    return inorder(root)

# Time: O(n) - visit all nodes
# Space: O(h) - recursion stack


# APPROACH 2: DFS with Min/Max Bounds (Alternative)
# --------------------------------------------------
# Track valid range for each node:

def isValidBST(self, root):
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return validate(node.left, min_val, node.val) and \
               validate(node.right, node.val, max_val)
    
    return validate(root, float('-inf'), float('inf'))

# Time: O(n)
# Space: O(h)


# WHEN TO USE EACH:
# -----------------
# ✅ Inorder: Clean, easy to understand, natural for BST
# ✅ Bounds: More explicit about constraints, generalizes better


# COMMON MISTAKES (MY MISTAKES):
# ------------------------------
# ❌ Only checking immediate children (misses the trap case!)
# ❌ Forgetting to update prev = node after comparison
# ❌ Saying O(1) space (forgot recursion stack = O(h)!)
# ❌ Using node.val <= prev instead of node.val <= prev.val
# ❌ Not handling prev = None case properly


# COMPLEXITY ANALYSIS:
# -------------------
# Time: O(n) - must visit all nodes to validate
# Space: O(h) - recursion call stack
#   - Balanced: O(log n)
#   - Skewed: O(n)

# 8. Kth Smallest Element in BST:
#    - Use inorder traversal (visits in sorted order)
#    - Track count as you visit nodes
#    - When count == k, store and return
#    - Structure: LEFT → process → RIGHT (critical order!)
#    - Can optimize to O(k) time with early stopping
#    - Time: O(k) best, O(n) worst
#    - Space: O(h) recursion stack
#    - Date: Oct 31, took ~25 min with structure reminder
#    - MY MISTAKE: Tried to overcomplicate with while loops
#    - KEY: Just follow inorder pattern, don't overthink!