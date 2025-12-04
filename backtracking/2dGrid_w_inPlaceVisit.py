# ---

# # 📋 **TEMPLATE 2: WORD SEARCH**

# ## Word Search (LC 79) - MEDIUM - Blind 75 ✅
# **Date Solved:** Nov 4, 2024 (Day 8)
# **Time Taken:** ~20 min (with 4 bug fixes)
# **Pattern:** Backtracking on 2D Grid + In-Place Visited Tracking

# ### Problem:
# Given m×n grid of characters and a word, return true if word exists in grid.
# - Word can be constructed from adjacent cells (up/down/left/right)
# - Same cell cannot be used twice in same word

# ### Approach:
# 1. Try every cell as potential starting point
# 2. From each cell, DFS in 4 directions matching word character by character
# 3. Track visited by MODIFYING board (mark as '#'), then RESTORE (backtrack!)
# 4. Track word_idx instead of building string (efficiency!)
# 5. Return True as soon as ANY path succeeds

# ### Time Complexity: O(m × n × 4^L)
# **Exponential!** Decision tree analysis:
# - Try every cell as start: O(m × n)
# - From each cell: 4 directions to explore
# - Go L levels deep (word length)
# - Each level branches 4 ways: 4^L paths worst case
# - **Total: O(m × n × 4^L)**

# ### Space Complexity: O(L)
# - Recursion stack depth: O(L) - maximum depth is word length
# - No extra visited set needed (in-place marking)
# - **Total: O(L)**

# ### Complete Solution:
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def backtrack(r, c, word_idx):
            # Base case: matched entire word
            if word_idx == len(word):
                return True
            
            # Base cases: invalid
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                board[r][c] != word[word_idx]):
                return False
            
            # Mark visited (MAKE CHOICE)
            temp = board[r][c]
            board[r][c] = '#'
            
            # Try 4 directions (RECURSE)
            for dr, dc in directions:
                if backtrack(r + dr, c + dc, word_idx + 1):
                    board[r][c] = temp  # Restore before returning
                    return True
            
            # Restore cell (BACKTRACK!)
            board[r][c] = temp
            return False
        
        # Try every cell as starting point
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        
        return False