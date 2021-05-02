class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def nodesWithoutSibling(root):
    if root is None:
        return
    if (root.left is None) and (root.right is not None):
        print(root.right.data)
    if (root.left is not None) and (root.right is None):
        print(root.left.data)
    nodesWithoutSibling(root.left)
    nodesWithoutSibling(root.right)
    pass


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
    root = Tree(rootData)
    root.left = takeInput()
    root.right = takeInput()
    return root


root = takeInput()
printTreeDetailed(root)
nodesWithoutSibling(root)