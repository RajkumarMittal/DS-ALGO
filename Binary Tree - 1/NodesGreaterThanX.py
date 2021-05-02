class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def largerThanX(root, x):
    if root is None:
        return 0
    leftSide = largerThanX(root.left, x)
    rightSide = largerThanX(root.right, x)
    if root.data > x:
        return leftSide + rightSide + 1
    return leftSide + rightSide


def takeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTree(rootData)
    root.left = takeInput()
    root.right = takeInput()
    return root


root = takeInput()
x = int(input())
print(largerThanX(root, x))
