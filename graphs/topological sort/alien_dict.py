# ## Alien Dictionary (LC 269) - HARD - Blind 75 ✅
# **Date Solved:** Nov 6, 2024 (Day 10)
# **Time Taken:** ~45 min (2nd Hard problem ever!)
# **Pattern:** Graph Building + Topological Sort (Course Schedule + String Comparison)

# ### Problem:
# Given sorted list of words in alien language, derive the order of characters in alien alphabet.
# Return the order as a string, or "" if no valid order exists.

# ### Key Insight - Two-Step Process:
# **Step 1 (HARD):** Build graph from string comparisons  
# **Step 2 (FAMILIAR):** Run topological sort (same as Course Schedule)

# **The challenge:** Converting strings → edges (NEW skill learned today!)

# ### Approach:

# **Part A: Build Graph (Compare Adjacent Words)**
# 1. Initialize graph with all unique characters
# 2. Compare each pair of adjacent words
# 3. Find FIRST differing character → that's your edge!
# 4. Stop after first difference (rest doesn't give ordering info)
# 5. Edge case: If word1 is longer but no difference found → INVALID

# **Part B: Topological Sort (DFS with 3 States)**
# 1. Same as Course Schedule (Day 7)
# 2. Detect cycles → return ""
# 3. Build result in reverse topological order
# 4. Reverse final result

# ### Time Complexity: O(C)
# Where C = total characters in all words combined
# - Build graph: O(C) - iterate through all characters
# - DFS: O(V + E) where V = unique chars, E = edges
# - Total: O(C) since V, E ≤ C

# ### Space Complexity: O(V + E)
# - Graph: O(V + E)
# - Recursion stack: O(V)
# - Sets: O(V)

# ### Complete Solution:
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if not words:
            return ""
        
        # Part A: Build graph from string comparisons
        graph = {char: [] for word in words for char in word}
        
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))
            
            # Find first differing character
            for j in range(min_len):
                if word1[j] != word2[j]:
                    # Found ordering: word1[j] comes before word2[j]
                    graph[word1[j]].append(word2[j])
                    break  # CRITICAL! Only first difference matters
            else:
                # No difference found in first min_len characters
                # If word1 is longer, it's invalid (e.g., "abc" before "ab")
                if len(word1) > len(word2):
                    return ""
        
        # Part B: Topological sort (DFS with 3 states)
        visiting = set()  # Currently exploring (state 1)
        visited = set()   # Finished processing (state 2)
        result = []
        
        def dfs(char):
            if char in visiting:
                return False  # Cycle detected!
            if char in visited:
                return True   # Already processed
            
            visiting.add(char)
            for neighbor in graph[char]:
                if not dfs(neighbor):
                    return False
            
            visiting.remove(char)
            visited.add(char)
            result.append(char)  # Post-order = reverse topological
            return True
        
        # Run DFS on all characters
        for char in graph:
            if char not in visited:
                if not dfs(char):
                    return ""  # Cycle = invalid ordering
        
        return ''.join(result[::-1])  # Reverse for correct order