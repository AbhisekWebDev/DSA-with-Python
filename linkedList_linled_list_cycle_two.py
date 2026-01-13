# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head) :

        slow = head
        fast = head

        hasCycle = False

        # detect cycle
        while fast != None and fast.next != None :
            fast = fast.next.next
            slow = slow.next

            if fast == slow :
                hasCycle = True 
                break
        
        if not hasCycle :
            return None # no cycle

        # find cycle length
        l = 0

        while slow.next != fast :
            slow = slow.next
            l += 1
        
        l += 1
        slow = slow.next

        # find cycle start
        slow = head
        fast = head

        # move fast ahead by cycle length
        for _ in range(l) :
            fast = fast.next

        # move both until they meet
        while slow != fast :
            slow = slow.next
            fast = fast.next
        
        return slow
    
# Create list: [3,2,0,-4], cycle at index 1
head = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # cycle here

sol = Solution()
cycle_node = sol.detectCycle(head)

print(cycle_node.val)  # Output: 2
