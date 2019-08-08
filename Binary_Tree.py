class BinaryTree:
    class Node:
        __slots__ = '_element', '_left', '_right'

        def __init__(self, element, left=None, right=None):
            self._element = element
            self._left = left
            self._right = right

    def __init__(self):
        self._root = None
        self._size = 0

    def maketree(self, element, left, right):
        self._root = self.Node(element, left=left._root, right=right._root)
        left._root = None
        right._root = None

    def levelorder(self):
        q = []
        t = self._root
        print(t._element, end='--')
        q.append(t)

        while q:
            t = q[0]
            del q[0]

            if t._left:
                print(t._left._element, end='--')
                q.append(t._left)

            if t._right:
                print(t._right._element, end='--')
                q.append(t._right)

    def inorder(self, root):
        if root:
            self.inorder(root._left)
            print(root._element, end='--')
            self.inorder(root._right)

    def preorder(self, root):
        if root:
            print(root._element, end='--')
            self.preorder(root._left)
            self.preorder(root._right)

    def postorder(self, root):
        if root:
            self.postorder(root._left)
            self.postorder(root._right)
            print(root._element, end='--')


a = BinaryTree()
b = BinaryTree()
c = BinaryTree()
d = BinaryTree()
e = BinaryTree()
f = BinaryTree()
g = BinaryTree()

b.maketree(50,a,a)
c.maketree(100,a,a)
d.maketree(10,b,a)
e.maketree(20,a,c)
f.maketree(40,e,a)
g.maketree(80,d,f)

g.levelorder()
print()
g.preorder(root=g._root)
print()
g.inorder(root=g._root)
print()
g.postorder(root=g._root)
print()