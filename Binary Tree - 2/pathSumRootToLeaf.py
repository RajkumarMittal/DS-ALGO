class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def rootToleafSum(root, k, lst):
    if root is None:
        return
    if root.left is None and root.right is None and root.data == k:
        print(*lst, root.data)
    lst.append(root.data)
    rootToleafSum(root.left, k-root.data, lst)
    rootToleafSum(root.right, k-root.data, lst)
    lst.pop()


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
rootToleafSum(root, 13, [])

