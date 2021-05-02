class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def heightTree(root):
    if root is None:
        return 0
    ls = heightTree(root.left)
    rs = heightTree(root.right)
    return max(ls, rs) + 1


def takeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTree(rootData)
    root.left = takeInput()
    root.right = takeInput()
    return root


root = takeInput()
print(heightTree(root))