# Clone Graph (LC 133)
# BLIND 75 ✅ | Medium | Graph Copy with HashMap
# TIME: Day 7: ~35 min (stuck on concept, used template)
#
# ═══════════════════════════════════════════════════════════════
# KEY INSIGHT:
# ═══════════════════════════════════════════════════════════════
# HashMap maps OLD nodes → NEW nodes (the copies)
# Queue holds OLD nodes to process (BFS on original graph)
# For each node: create copy if needed, connect COPIES together
#
# THE MAGIC LINE:
# old_to_new[current].neighbors.append(old_to_new[neighbor])
#     ^^^ copy              ^^^           ^^^ copy
# Translation: "Copy's neighbors = copies of original's neighbors"
#
# ═══════════════════════════════════════════════════════════════
# COMPLEXITY:
# ═══════════════════════════════════════════════════════════════
# Time: O(V + E) - visit all nodes + process all edges
# Space: O(V) - hashmap stores all nodes, queue holds up to V nodes
#
# ═══════════════════════════════════════════════════════════════
# MY CONFUSION: How does the copying work? Original vs cloned?
# MY UNDERSTANDING: Two separate graphs in memory. HashMap bridges
#                   them. We traverse original graph (queue) but
#                   build cloned graph (old_to_new values).