# Making node
class Node:
    def __init__(self, key):
        self.left=None
        self.right=None
        self.item = key


# Inorder will traverse in [Left, root , right]
def InorderTra(root):

    if root:

        # this will move until the left is present
        InorderTra(root.left)

        print(root.item)

        # traverse the right part
        InorderTra(root.right)


# PREORDER WORKS IN ["ROOT" -> LEFT -> RIGHT]
def PreorderTrav(root):
    if root:

        print(root.item)

        PreorderTrav(root.left)

        PreorderTrav(root.right)


# THIS WORK IN THE FORMAT("LEFT" -> "RIGHT" -> "ROOT")
def PostOrderTrav(root):
    if root:
        PostOrderTrav(root.left)

        PostOrderTrav(root.right)

        print(root.item)



if __name__ == "__main__":

    root = Node(1) 
    root.left      = Node(2) 
    root.right     = Node(3) 
    root.left.left  = Node(4) 
    root.left.right  = Node(5) 
    
    print("This is for Inorder Traversal:")
    InorderTra(root)


    print("\n This is for Preorder Traversal:")
    PreorderTrav(root)

    print("This is for POSTorder Traversal:")
    PostOrderTrav(root)
