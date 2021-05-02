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


def mergeTwo(l1, l2):
    l1_lenght = length(l1)
    l2_lenght = length(l2)
    if(l1_lenght and l2_lenght) is None:
        return None
    c1 = l1
    c2 = l2
    if l1_lenght <= l2_lenght:
        while l1_lenght:
            if c1.data <= c2.data:
                temp = c1.next
                c1.next = c2
                c2.next = temp


    pass


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


l1 = takeInput()
l2 = takeInput()
print("L1")
printLL(l1)
print("L2")
printLL(l2)
print("Merge")
l = mergeTwo(l1, l2)
printLL(l)
