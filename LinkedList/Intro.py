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


def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)
        if head is None:
            head = newNode
            tail = head
        else:
            tail.next = newNode
            tail = newNode
    return head


def printLL(head):
    while head is not None:
        print(str(head.data) + "-->", end=" ")
        head = head.next
    print(None)


head = takeInput()
printLL(head)

