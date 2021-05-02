class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def length(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count


def deleteNodeRec(head, i):
    if i < 0 or i >= length(head):
        return head
    if head is None:
        return None
    if i == 0:
        head = head.next
        return head
    head.next = deleteNodeRec(head.next, i-1)
    return head


def deleteNode(head, i):
    if head is None:
        return
    if i >= length(head) or i < 0:
        return head
    if i == 0:
        head = head.next
        return head
    curr = head
    prev = None
    while i != 0:
        prev = curr
        curr = curr.next
        i -= 1
    prev.next = curr.next
    return head


def takeInput():
    inputList = [int(i) for i in input().split()]
    head = None
    tail = None
    for curr in inputList:
        if curr == -1:
            break
        newNode = Node(curr)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = tail.next
    return head


def printLL(head):
    while head is not None:
        print(str(head.data) + "-->", end=" ")
        head = head.next
    print(None)


head = takeInput()
i = int(input())
printLL(head)
print("Delete iter")
head = deleteNode(head, i)
printLL(head)
head = takeInput()
i = int(input())
print("Delete rec")
head = deleteNodeRec(head, i)
printLL(head)
