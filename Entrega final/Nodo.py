class Node(object):
    def __init__(self, value, root=None):
        self.value = value
        if(root):
            self.root = root
        else:
            self.root = None
        self.left = None
        self.right = None

        self.nullable = None
        self.firstPos = []
        self.lastPos = []
    
    def isNullable(self):
        return self.nullable
    
    def getFirstPos(self):
        return self.firstPos
    
    def getLastPos(self):
        return self.lastPos
    
    def setNullable(self, nullable):
        self.nullable = nullable
    
    def addFirstPos(self, pos):
        self.firstPos += pos
    
    def addLastPos(self, pos):
        self.lastPos += pos

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
    
    def info(self):
        print(f"""
        Value = {self.value}
        Nullable = {self.nullable}
        FirstPos = {self.firstPos}
        LastPos = {self.lastPos}
        """)


# MAAAIN
'''
root=Node(None)
root.setLeft('+',root)

actual=root.getLeft()
actual=actual.getRoot()
print(actual.getValue())
'''