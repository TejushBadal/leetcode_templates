# Construct Binary Tree from Preorder and Inorder Traversal (LC 105)
# BLIND 75 ✅ | Medium | Tree Construction Pattern
# TIME: Day 6: ~10 min (with algorithm guidance)
# 
# ═══════════════════════════════════════════════════════════════
# KEY INSIGHTS:
# ═══════════════════════════════════════════════════════════════
# 1. First element of PREORDER = ROOT (Root→Left→Right)
# 2. Find root in INORDER splits it: [LEFT] ROOT [RIGHT]
# 3. Size of left_inorder tells us how to split preorder
# 4. Recurse on left and right subtrees with matching slices
#
# ═══════════════════════════════════════════════════════════════
# COMPLEXITY:
# ═══════════════════════════════════════════════════════════════
# Time:  O(n²) naive (linear search for root each time)
#        O(n) optimized (hashmap for O(1) lookup)
# Space: O(n) - recursion stack O(h) + hashmap O(n)
#
# ═══════════════════════════════════════════════════════════════
# ALGORITHM:
# ═══════════════════════════════════════════════════════════════
def buildTree(preorder, inorder):
    # Base case
    if not preorder or not inorder:
        return None
    
    # Step 1: Root is first element of preorder
    root_val = preorder[0]
    root = TreeNode(root_val)
    
    # Step 2: Find root in inorder (use hashmap for O(1))
    # OPTIMIZATION: Build hashmap ONCE outside recursion
    inorder_map = {val: idx for idx, val in enumerate(inorder)}
    root_idx = inorder_map[root_val]
    
    # Step 3: Split inorder into left and right
    left_inorder = inorder[:root_idx]
    right_inorder = inorder[root_idx+1:]  # Skip root!
    
    # Step 4: Split preorder using size of left_inorder
    left_size = len(left_inorder)
    left_preorder = preorder[1:1+left_size]  # Skip root
    right_preorder = preorder[1+left_size:]
    
    # Step 5: Recursively build subtrees
    root.left = buildTree(left_preorder, left_inorder)
    root.right = buildTree(right_preorder, right_inorder)  # WATCH TYPO!
    
    return root
# ═══════════════════════════════════════════════════════════════
# COMMON BUGS:
# ═══════════════════════════════════════════════════════════════
# ❌ Off-by-one in slicing (forgetting to skip root)
# ❌ Typo: passing left_inorder to right recursion (my Day 6 bug!)
# ❌ Wrong preorder split (forgetting to use left_size)
#
# ═══════════════════════════════════════════════════════════════
# VARIATIONS:
# ═══════════════════════════════════════════════════════════════
# - Construct from Postorder + Inorder (root is LAST in postorder)
# - Can't construct from Preorder + Postorder alone (need inorder!)
#
# ═══════════════════════════════════════════════════════════════
# MY NOTES:
# ═══════════════════════════════════════════════════════════════
# [Add your personal notes here]
#
# MY MISTAKE: Passed left_inorder to right subtree (typo)
# MY KEY INSIGHT: Size of left_inorder determines preorder split
# DIFFICULTY FELT: 6/10 with guidance, 8/10 without