# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int) :

        curr = head

        length = 0

        while curr :
            length += 1
            curr = curr.next
        
        # if head needs to be deleted
        if n == length:
            return head.next
        
        # length nikala 

        # ab length me se n minus kr denge to delete krne wala node mil jyga

        del_node = length - n

        # find node before deletion
        curr = head

        for _ in range(del_node - 1) :
            curr = curr.next

        curr.next = curr.next.next
    
        return head

# ---------------- Helper Functions ----------------

def create_linked_list(arr) :
    if not arr:
        return None

    head = ListNode(arr[0])
    curr = head

    for val in arr[1:] :
        curr.next = ListNode(val)
        curr = curr.next

    return head


def print_linked_list(head) :
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


# ---------------- Test Cases ----------------

sol = Solution()

# Test Case 1
head1 = create_linked_list([1, 2, 3, 4, 5])
print("Original:")
print_linked_list(head1)
head1 = sol.removeNthFromEnd(head1, 2)
print("After removing 2nd from end:")
print_linked_list(head1)
print()

# Test Case 2 (remove head)
head2 = create_linked_list([1, 2])
print("Original:")
print_linked_list(head2)
head2 = sol.removeNthFromEnd(head2, 2)
print("After removing 2nd from end:")
print_linked_list(head2)
print()

# Test Case 3 (single node)
head3 = create_linked_list([1])
print("Original:")
print_linked_list(head3)
head3 = sol.removeNthFromEnd(head3, 1)
print("After removing 1st from end:")
print_linked_list(head3)
print()

# Test Case 4
head4 = create_linked_list([10, 20, 30, 40])
print("Original:")
print_linked_list(head4)
head4 = sol.removeNthFromEnd(head4, 1)
print("After removing last node:")
print_linked_list(head4)