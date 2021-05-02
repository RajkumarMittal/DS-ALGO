class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def numberOfLeafs(root):
    if root is None:
        return 0
    if(root.left and root.right) is None:
        return 1
    return numberOfLeafs(root.left) + numberOfLeafs(root.right)


def takeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTree(rootData)
    root.left = takeInput()
    root.right = takeInput()
    return root


root = takeInput()
print(numberOfLeafs(root))