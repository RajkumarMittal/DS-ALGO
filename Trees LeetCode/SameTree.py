class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isSame(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.data != root2.data:
        return False
    ls = isSame(root1.left, root2.left)
    rs = isSame(root1.right, root2.right)
    return ls and rs
    pass


def printTreeDetailed(root):
    if root is None:
        return None
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


root1 = takeInput()
root2 = takeInput()
print("Tree1")
printTreeDetailed(root1)
print("Tree2")
printTreeDetailed(root2)
print(isSame(root1, root2))