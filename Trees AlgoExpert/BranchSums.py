class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def branchSum(root,lst=[0]):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        lst[-1] += 1
        print(lst[-1] + root.data)
    branchSum(root.left, lst)
    branchSum(root.right, lst)
    lst[-1] - root.data


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
branchSum(root)