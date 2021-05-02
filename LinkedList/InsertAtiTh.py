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


def insert_ith(head, i, data):
    if head is None:
        return
    if(i < 0) or (i > length(head)):
        return head
    newNode = Node(data)
    if i == 0:
        newNode.next = head
        return newNode
    curr = head
    prev = None
    while i != 0:
        prev = curr
        curr = curr.next
        i -= 1
    prev.next = newNode
    newNode.next = curr
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
head = insert_ith(head, i, 100)
print("After insertion")
printLL(head)


