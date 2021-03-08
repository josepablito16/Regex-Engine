class Node(object):
    def __init__(self, value, root=None):
        self.value = value
        if(root):
            self.root = root
        else:
            self.root = None
        self.left = None
        self.right = None

    def getValue(self):
        return self.value

    def getRoot(self):
        return self.root

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def setRight(self, value, root):
        self.right = Node(value, root)

    def setLeft(self, value, root):
        self.left = Node(value, root)

    def setValue(self, value):
        self.value = value


# MAAAIN
'''
root=Node(None)
root.setLeft('+',root)

actual=root.getLeft()
actual=actual.getRoot()
print(actual.getValue())
'''