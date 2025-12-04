# ## Unique Paths (LC 62) - MEDIUM - Blind 75 ✅
# **Date Solved:** Nov 5, 2024 (Day 9)
# **Time Taken:** 11 min (first 2D DP exposure!)
# **Pattern:** 2D Grid DP - Path Counting

# ### Problem:
# Robot on m×n grid. Start at top-left (0,0), goal is bottom-right (m-1, n-1).
# - Can only move RIGHT or DOWN
# - Count number of unique paths to reach goal

# ### Key Insight - 2D Extension of 1D DP:
# 1D DP (Climbing Stairs): dp[i] = dp[i-1] + dp[i-2]
# (look back in line)

# 2D Grid DP (Unique Paths): dp[i][j] = dp[i-1][j] + dp[i][j-1]
# (look at cell above + cell left)

# ### Approach:
# 1. **State:** dp[i][j] = number of ways to reach cell (i,j) from (0,0)
# 2. **Base cases:**
#    - Top row: dp[0][j] = 1 (only one way: keep moving right)
#    - Left column: dp[i][0] = 1 (only one way: keep moving down)
# 3. **Recurrence:** dp[i][j] = dp[i-1][j] + dp[i][j-1]
#    - Ways from above + ways from left
# 4. **Answer:** dp[m-1][n-1]

# ### Visualization (3×3 grid):
# Start
# 1 → 1 → 1 ← Top row: all 1
# ↓ ↓ ↓
# 1 → 2 → 3 ← dp[1][1] = 1+1=2, dp[1][2] = 1+2=3
# ↓ ↓ ↓
# 1 → 3 → 6 ← dp[2][1] = 2+1=3, dp[2][2] = 3+3=6
# ↑
# Goal (6 paths)


### Time Complexity: O(m × n)
# - Fill m×n grid once
# - Each cell: O(1) computation (sum two values)

# ### Space Complexity: O(m × n)
# - 2D DP array of size m×n
# - Can optimize to O(n) with rolling array (only need previous row)

### Complete Solution:
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Edge case: single row or column
        if m == 1 or n == 1:
            return 1
        
        # Initialize m×n grid
        dp = [[0] * n for _ in range(m)]
        
        # Base case: top row
        for col in range(n):
            dp[0][col] = 1
        
        # Base case: left column
        for row in range(m):
            dp[row][0] = 1
        
        # Fill grid with recurrence
        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[m-1][n-1]


# MY KEY INSIGHTS:
# 2D DP = natural extension of 1D DP - instead of looking back in line, look at adjacent cells
# Grid initialization: [[0]*n for _ in range(m)] creates m rows, n columns
# Base cases are edges: Top row and left column (only one way to reach them)
# Current cell depends on neighbors: Above and left (can't look right/down - haven't computed yet!)
# Edge case optimization: m==1 or n==1 → return 1 immediately (trivial case)
# Loop ranges matter: Start from (1,1) to skip base cases already filled

#MASTER TEMPLATE
# Step 1: Define state
# dp[i][j] = answer for subproblem at position (i,j)

# Step 2: Initialize grid
dp = [[0] * n for _ in range(m)]

# Step 3: Fill base cases
# (edges, corners, or specific cells with known values)

# Step 4: Nested loops for recurrence
for i in range(1, m):  # Skip base case rows
    for j in range(1, n):  # Skip base case cols
        dp[i][j] = f(dp[i-1][j], dp[i][j-1], ...)  # Recurrence

# Step 5: Return answer
#return dp[m-1][n-1]  # Or wherever answer is