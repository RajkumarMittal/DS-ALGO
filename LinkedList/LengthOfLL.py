class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def lengthRec(head):
    if head is None:
        return 0
    return lengthRec(head.next) + 1


def length(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count


def takeInput():
    inputList = [int(i) for i in input().strip().split()]
    head = None
    tail = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)
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
printLL(head)
print(length(head))
print("----")
print(lengthRec(head))
