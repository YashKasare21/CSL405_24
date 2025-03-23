class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head, k):
    if not head or not head.next or k == 0:
        return head
    
    
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1
    
    
    tail.next = head
    
   
    k = k % length
    steps_to_new_head = length - k
    new_tail = head
    for _ in range(steps_to_new_head - 1):
        new_tail = new_tail.next
    
    
    new_head = new_tail.next
    new_tail.next = None
    
    return new_head


def list_to_linkedlist(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linkedlist_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


arr = list(map(int, input("Enter the elements of the linked list separated by spaces: ").split()))
k = int(input("Enter the value of k: "))

head = list_to_linkedlist(arr)
new_head = rotateRight(head, k)
print("Rotated Linked List:", linkedlist_to_list(new_head))
