class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def removeLeaf(root):
    if root is None:
        return
    if(root.left and root.right) is None:
        return None
    root.left = removeLeaf(root.left)
    root.right = removeLeaf(root.right)
    return rootz


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
root = removeLeaf(root)
printTreeDetailed(root)