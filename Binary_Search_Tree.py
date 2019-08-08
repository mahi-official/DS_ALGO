class BST:
    class Node:
        __slots__ = '_element', '_left', '_right'

        def __init__(self, element, left=None, right=None):
            self._element = element
            self._left = left
            self._right = right

    def __init__(self):
        self._root = None
        self._size = 0

    def insert(self, element):
        troot = self._root
        temp = None
        while troot:
            temp = troot
            if element < troot._element:
                troot = troot._left
            elif element > troot._element:
                troot = troot._right
        node = self.Node(element)
        if self._root:
            if element < temp._element:
                temp._left = node
            else:
                temp._right = node
        else:
            self._root = node

    def recurinsert(self, root, element):
        if root ==None:
            node = self.Node(element)
            return node

        if element < root._element:
            root._left = self.recurinsert(root._left, element)
        if element > root._element:
            root._right = self.recurinsert(root._right, element)

        return root

    def search(self, element):
        temp = self._root
        while temp:
            if element < temp._element:
                temp = temp._left
            elif element > temp._element:
                temp = temp._right
            else:
                return True
        return False


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


b = BST()
b._root = b.recurinsert(None, 70)
b.recurinsert(b._root, 30)
b.recurinsert(b._root, 90)
b.recurinsert(b._root, 20)
b.recurinsert(b._root, 80)
b.recurinsert(b._root, 60)
b.recurinsert(b._root, 30)

b.levelorder()
print()
b.preorder(root=b._root)
print()
b.inorder(root=b._root)
print()
b.postorder(root=b._root)
print()
print(b.search(60))
