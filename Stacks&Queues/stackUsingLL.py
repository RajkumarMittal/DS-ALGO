class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SStack:
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, item):
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode
        self.count += 1

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return 0
        data = self.head.data
        self.head = self.head.next
        self.count -= 1
        return data

    def top(self):
        if self.isEmpty():
            print("Stack is Empty")
            return 0
        return self.head.data

    def size(self):
        return self.count

    def isEmpty(self):
        return self.size() == 0


s = SStack()
s.push(10)
s.push(20)
s.push(30)
# s.printLL()
print(s.top())
print(s.size())