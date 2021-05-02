# If height difference is more than 1, then tree is unbalanced.
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isbalanced(root):
    if root is None:
        return 0, True
    lh, ls = isbalanced(root.left)
    rh, rs = isbalanced(root.right)
    h = 1 + max(lh, rh)
    if(lh - rh > 1) or (rh - lh > 1):
        return h, False
    return h, ls and rs


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
h, check = isbalanced(root)
print(check)