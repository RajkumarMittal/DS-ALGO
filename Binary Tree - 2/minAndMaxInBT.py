class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def minMax(root):
    if root is None:
        return 10**6, -10**6
    m1, m2 = minMax(root.left)
    m3, m4 = minMax(root.right)
    return min(m1, m3, root.data), max(m2, m4, root.data)


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
minVal, maxVal = minMax(root)
print("Min Value in the Tree :", minVal)
print("Max Value in the Tree :", maxVal)
