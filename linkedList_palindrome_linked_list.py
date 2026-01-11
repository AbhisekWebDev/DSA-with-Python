# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head) -> bool:

        if not head or not head.next:
            return True

        # Step 1: Find middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3: Compare halves
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True

def build_list(arr):
    head = None
    curr = None
    for val in arr:
        if not head:
            head = ListNode(val)
            curr = head
        else:
            curr.next = ListNode(val)
            curr = curr.next
    return head

head = build_list([1])
# Expected: True

head = build_list([1])
# Expected: True

head = build_list([1, 2])
# Expected: False

head = build_list([1, 2, 1])
# Expected: True

head = build_list([1, 2, 2, 1])
# Expected: True

head = build_list([1, 2, 3])
# Expected: False

head = build_list([1, 2, 3, 4])
# Expected: False

head = build_list([1, 1, 2, 1])
# Expected: False

head = build_list([5, 5, 5, 5, 5])
# Expected: True

sol = Solution()

tests = [
    [1],
    [1,1],
    [1,2],
    [1,2,1],
    [1,2,2,1],
    [1,2,3],
    [1,2,3,4],
    [1,1,2,1],
    [5,5,5,5,5],
    [1,2,3,4,5,4,3,2,1]
]

for t in tests:
    head = build_list(t)
    print(t, "->", sol.isPalindrome(head))
