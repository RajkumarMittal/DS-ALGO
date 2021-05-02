class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# def height(root):
#     if root is None:
#         return 0
#     return max(height(root.left), height(root.right)) + 1


def diameter2(root):
    if root is None:
        return 0, 0
    lh, ld = diameter2(root.left)
    rh, rd = diameter2(root.right)
    return 1+max(lh, rh), max(lh+rh+1, lh, rh, ld, rd)


def diameter(root):
    h, d = diameter2(root)
    return d


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
print(diameter(root))