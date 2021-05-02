class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def mirror(root):
    if root is None:
        return
    leftSide = mirror(root.left)
    rightSide = mirror(root.right)
    root.left = rightSide
    root.right = leftSide
    return root


def printTreeDetailed(root):
    if root is None:
        return
    print(root.data, end=":")
    if root.left is not None:
        print("l", root.left.data, end=",")
    if root.right is not None:
        print("R", root.right.data, end=" ")
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)


def takeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTree(rootData)
    root.left = takeInput()
    root.right = takeInput()
    return root


root = takeInput()
printTreeDetailed(root)
root = mirror(root)
print("-------------")
printTreeDetailed(root)