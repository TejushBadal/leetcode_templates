# PATTERN: Fast/Slow Pointers (Floyd's Cycle Detection)
# PROBLEM: LC 141 - Linked List Cycle

# TEMPLATE:
def hasCycle(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next  # Or start both at head
    
    while fast and fast.next:
        if slow == fast:
            return True
        
        slow = slow.next
        fast = fast.next.next
    
    return False

# COMPLEXITY: O(n) time, O(1) space

# WHY IT WORKS:
# - If no cycle: fast reaches None → return False
# - If cycle exists: fast eventually catches slow
# - Fast closes gap by 1 position per iteration in the cycle

# KEY CHECKS:
# - Must check "fast and fast.next" to prevent crashes
# - fast.next ensures we can safely do fast.next.next

# ALTERNATIVE: Start both at head, check AFTER moving (equally valid)

# WHEN TO USE:
# - Cycle detection in linked lists
# - Finding middle of linked list (slow will be at middle when fast reaches end)
# - Finding start of cycle (LC 142 - extended version)

# SIMILAR PROBLEMS:
# - LC 142: Linked List Cycle II (return where cycle begins)
# - LC 876: Middle of Linked List
# - LC 287