# If height difference is more than 1, then tree is unbalanced.
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def isbalanced(root):
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if(lh - rh > 1) or (rh - lh > 1):
        return False
    return isbalanced(root.left) and isbalanced(root.right)


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
print(isbalanced(root))