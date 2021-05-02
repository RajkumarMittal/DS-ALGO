class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def elementRec(head, i):
    if head is None:
        return None
    if i == 0:
        return head.data
    return elementRec(head.next, i-1)
    pass


def element(head, i):
    count = 0
    currHead = head
    while currHead is not None:
        if count == i:
            print(currHead.data)
        count += 1
        currHead = currHead.next
    return


def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currentData in inputList:
        if currentData == -1:
            break
        newNode = Node(currentData)
        if head is None:
            head = newNode
            tail = newNode
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
i = int(input("Enter the ith position : "))
result = element(head, i)
if result is None:
    print(None)
print("---")
print(elementRec(head, i))

