# Count Good Nodes in Binary Tree (LC 1448)
# Medium | DFS with Path Tracking
# TIME: Day 6: ~15 min
# 
# ═══════════════════════════════════════════════════════════════
# KEY INSIGHT:
# ═══════════════════════════════════════════════════════════════
# Track MAX value on path from root
# Node is "good" if node.val >= max_so_far
# Similar to Validate BST bounds pattern!
#
# ═══════════════════════════════════════════════════════════════
# RECURSION PATTERN: Count from Subtrees
# ═══════════════════════════════════════════════════════════════
# 1. Current node's contribution (0 or 1)
# 2. Add left subtree's TOTAL COUNT (returned from recursive call)
# 3. Add right subtree's TOTAL COUNT (returned from recursive call)
# 4. Return combined total to parent
#
# Each recursive call has its OWN count variable on the stack!
#
# ═══════════════════════════════════════════════════════════════
# COMPLEXITY:
# ═══════════════════════════════════════════════════════════════
# Time: O(n) - visit all nodes
# Space: O(h) - recursion call stack
#        O(log n) balanced, O(n) skewed
#
# ═══════════════════════════════════════════════════════════════
# MY NOTES:
# ═══════════════════════════════════════════════════════════════
# MY CONFUSION: How does count accumulate across recursive calls?
# MY UNDERSTANDING: Each call has its own count. When we do 
#                   count += dfs(child), we're adding the RETURN 
#                   VALUE (which is that subtree's total count).
#                   Not modifying a shared global!