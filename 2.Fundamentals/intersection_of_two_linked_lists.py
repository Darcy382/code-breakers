class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# First Attempt
def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
    currentA = headA
    currentB = headB
    id_set = set()

    while currentA or currentB:
        if currentA:
            old_length = len(id_set)
            id_set.add(id(currentA))
            if len(id_set) == old_length:
                return currentA
            currentA = currentA.next
        if currentB:
            old_length = len(id_set)
            id_set.add(id(currentB))
            if len(id_set) == old_length:
                return currentB
            currentB = currentB.next
    return None


# Second attempt time O(n), space O(1)
def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1 = headA
        p2 = headB

        while (p1 or p2) and p1 is not p2:
            if p1:
                p1 = p1.next
            else:
                p1 = headB
            if p2:
                p2 = p2.next
            else:
                p2 = headA

        return p1




