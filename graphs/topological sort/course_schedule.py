# Course Schedule (LC 207)
# BLIND 75 ✅ | Medium | Cycle Detection in Directed Graph | CRITICAL BLOOMBERG
# TIME: Day 7: ~20 min (with template guidance, need independent review)
# MARKED FOR: Day 11 review (re-solve from scratch)
# 
# ═══════════════════════════════════════════════════════════════
# PROBLEM TYPE: Topological Sort / Cycle Detection
# ═══════════════════════════════════════════════════════════════
# Given: n courses (0 to n-1), prerequisites = [[a,b]] means "to take a, must finish b"
# Question: Can you finish all courses? (Is there a valid ordering?)
# Answer: YES if no cycles (topological order exists), NO if cycle exists
#
# ═══════════════════════════════════════════════════════════════
# KEY INSIGHT:
# ═══════════════════════════════════════════════════════════════
# Cycle in directed graph = deadlock (course A needs B, B needs A)
# Use DFS with 3 STATES to detect cycles:
#   0 = UNVISITED (white) - not processed yet
#   1 = VISITING (gray) - currently in recursion stack
#   2 = VISITED (black) - fully processed, no cycle found
#
# CYCLE DETECTION: If you reach a node that's VISITING (state=1) → CYCLE!
#   (You've looped back to a node you're still processing)
#
# ═══════════════════════════════════════════════════════════════
# APPROACH: DFS with States
# ═══════════════════════════════════════════════════════════════
def canFinish(numCourses, prerequisites):
    # Step 1: Build adjacency list
    # Graph: prereq → [courses that depend on prereq]
    graph = {i: [] for i in range(numCourses)}
    for course, prereq in prerequisites:
        graph[prereq].append(course)  # Edge: prereq → course
    
    # Step 2: Initialize states
    state = [0] * numCourses
    
    # Step 3: DFS with cycle detection
    def dfs(course):
        if state[course] == 1:  # VISITING → cycle found!
            return False
        if state[course] == 2:  # VISITED → already checked, no cycle
            return True
        
        state[course] = 1  # Mark as VISITING
        
        # Check all neighbors (courses that depend on this one)
        for next_course in graph[course]:
            if not dfs(next_course):
                return False
        
        state[course] = 2  # Mark as VISITED (CRITICAL - don't forget!)
        return True
    
    # Step 4: Check all courses (graph might be disconnected)
    for course in range(numCourses):
        if state[course] == 0:  # Only check unvisited
            if not dfs(course):
                return False
    
    return True

# ═══════════════════════════════════════════════════════════════
# ALTERNATIVE APPROACH: BFS with In-Degree (Kahn's Algorithm)
# ═══════════════════════════════════════════════════════════════
# 1. Count in-degree for each node (# of prerequisites)
# 2. Start with nodes with in-degree 0 (no prerequisites)
# 3. Process: decrement neighbors' in-degree, add to queue if 0
# 4. If processed all nodes → no cycle, else cycle exists
#
# Same complexity, more intuitive for some people
#
# ═══════════════════════════════════════════════════════════════
# COMPLEXITY:
# ═══════════════════════════════════════════════════════════════
# Time: O(V + E) where V = numCourses, E = len(prerequisites)
#       Visit all nodes + process all edges
# Space: O(V + E) - adjacency list + states array + recursion stack
#
# ═══════════════════════════════════════════════════════════════
# CRITICAL BUGS TO AVOID:
# ═══════════════════════════════════════════════════════════════
# ❌ Forgetting to set state[course] = 2 before returning True
#    (optimization won't work, might cause issues in variations)
# ❌ Not checking disconnected components (missing outer for loop)
# ❌ Confusing edge direction (prereq → course, not course → prereq)
#
# ═══════════════════════════════════════════════════════════════
# VARIATIONS / RELATED PROBLEMS:
# ═══════════════════════════════════════════════════════════════
# - Course Schedule II (LC 210): Return actual ordering (not just True/False)
# - Alien Dictionary (LC 269): Build graph from alien language ordering
# - Task Scheduler: Similar dependency problem
#
# BLOOMBERG FREQUENCY: ★★★★★ (VERY HIGH - dependency problems common!)
#
# ═══════════════════════════════════════════════════════════════
# MY NOTES:
# ═══════════════════════════════════════════════════════════════
# MY MISTAKE: Forgot to add states[course] = 2 before return True
# MY KEY INSIGHT: State 1 (visiting) in recursion stack = cycle detector
#                 If we encounter a gray node, we've looped back!
# MY CONFUSION: Edge direction - prereq→course (after prereq, can take course)
# DIFFICULTY FELT: 7/10 (concept is complex, needed template guidance)