def areMirror(root1, root2):
    if (root1 == None and root2 == None):
        return True
    if (root1 != None and root2 != None):
        if (root1.data == root2.data):
            return areMirror(root1.left, root2.right) and areMirror(root1.right, root2.left)
    return False
