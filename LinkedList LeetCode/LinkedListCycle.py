class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def check(head):
    if head is None:
        return False
    prev = head
    forw = head
    while forw is not None and forw.next is not None:
        forw = forw.next.next
        prev = prev.next
        if forw == prev:
            return True
    return False


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
print("List")
printLL(head)
result = check(head)
print(result)


