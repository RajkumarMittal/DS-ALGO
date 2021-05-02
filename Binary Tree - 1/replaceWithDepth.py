class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def replaceWithLevel(root, count=0):
    if root is None:
        return None
    root.data = count
    replaceWithLevel(root.left, count+1)
    replaceWithLevel(root.right, count+1)
    return root

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
print("---------")
root = replaceWithLevel(root)
printTreeDetailed(root)

