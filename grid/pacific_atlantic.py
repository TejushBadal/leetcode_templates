# Pacific Atlantic Water Flow (LC 417)
# BLIND 75 ✅ | Medium | Reverse DFS from Boundaries
# TIME: Day 7: 35 min (25 initial approach + 10 cleaner rewrite)
# MARKED FOR: Day 11 review
# 
# ═══════════════════════════════════════════════════════════════
# PROBLEM TYPE: Multi-Source DFS/BFS on Grid
# ═══════════════════════════════════════════════════════════════
# Given: m×n grid of heights (topographic map)
# Pacific ocean: touches top + left edges
# Atlantic ocean: touches bottom + right edges
# Water flows: current → adjacent if adjacent_height ≤ current_height
# Question: Which cells can flow to BOTH oceans?
#
# ═══════════════════════════════════════════════════════════════
# KEY INSIGHT: REVERSE THINKING!
# ═══════════════════════════════════════════════════════════════
# ❌ NAIVE: For each cell, check if can reach both oceans → O((m×n)²)
# ✅ OPTIMAL: Start FROM oceans, flow BACKWARDS (uphill!) → O(m×n)
#
# Why backwards works:
# - If water flows FROM cell TO ocean → ocean can "reach" cell
# - Start from ocean edges, DFS inward (going uphill: next >= current)
# - Collect two sets: pacific_reachable, atlantic_reachable
# - Answer = intersection of both sets
#
# ═══════════════════════════════════════════════════════════════
# APPROACH:
# ═══════════════════════════════════════════════════════════════
def pacificAtlantic(heights):
    if not heights:
        return []
    
    rows, cols = len(heights), len(heights[0])
    pacific = set()
    atlantic = set()
    
    def dfs(r, c, visited):
        visited.add((r, c))
        
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = r + dr, c + dc
            
            # Check: bounds + not visited + can go uphill
            if (0 <= nr < rows and 0 <= nc < cols and
                (nr, nc) not in visited and
                heights[nr][nc] >= heights[r][c]):  # ← UPHILL!
                dfs(nr, nc, visited)
    
    # DFS from Pacific edges (top + left)
    for c in range(cols):
        dfs(0, c, pacific)  # Top row
    for r in range(rows):
        dfs(r, 0, pacific)  # Left column
    
    # DFS from Atlantic edges (bottom + right)
    for c in range(cols):
        dfs(rows-1, c, atlantic)  # Bottom row
    for r in range(rows):
        dfs(r, cols-1, atlantic)  # Right column
    
    # Return intersection (cells reachable from BOTH oceans)
    return list(pacific & atlantic)

# ═══════════════════════════════════════════════════════════════
# COMPLEXITY:
# ═══════════════════════════════════════════════════════════════
# Time: O(m × n) - each cell visited at most twice (once per ocean)
# Space: O(m × n) - two sets + recursion stack
#
# ═══════════════════════════════════════════════════════════════
# CRITICAL DETAILS:
# ═══════════════════════════════════════════════════════════════
# - Flow condition: heights[next] >= heights[current] (UPHILL from ocean)
# - Corners get visited twice (e.g., (0,0) in top row AND left col)
#   but set handles duplicates automatically
# - Pass visited set to DFS (cleaner than returning sets)
#
# ═══════════════════════════════════════════════════════════════
# MY NOTES:
# ═══════════════════════════════════════════════════════════════
# MY MISTAKE: Initial approach overcomplicated (returning sets from DFS)
#             Cleaner to pass set and modify directly
# MY KEY INSIGHT: Reverse thinking - start from goal and work backwards!
#                 Avoids checking every cell multiple times
# DIFFICULTY FELT: 7/10 (concept is tricky, needed cleaner structure)