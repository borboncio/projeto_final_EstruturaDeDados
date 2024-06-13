class NodeTree:
    def __init__(self, item):
        self.key = item
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_rec(self.root, key)

    def _insert_rec(self, root, key):
        if root is None:
            return NodeTree(key)
        if key.nome < root.key.nome:
            root.left = self._insert_rec(root.left, key)
        elif key.nome > root.key.nome:
            root.right = self._insert_rec(root.right, key)
        return root

    def search(self, nome):
        return self._search_rec(self.root, nome)

    def _search_rec(self, root, nome):
        if root is None:
            return None
        if nome == root.key.nome:
            return root
        elif nome < root.key.nome:
            return self._search_rec(root.left, nome)
        else:
            return self._search_rec(root.right, nome)

    def inorder(self):
        result = []
        self._inorder_rec(self.root, result)
        return result

    def _inorder_rec(self, root, result):
        if root:
            self._inorder_rec(root.left, result)
            result.append(root.key)
            self._inorder_rec(root.right, result)

    def delete(self, nome):
        self.root = self._delete_rec(self.root, nome)

    def _delete_rec(self, root, nome):
        if root is None:
            return root
        if nome < root.key.nome:
            root.left = self._delete_rec(root.left, nome)
        elif nome > root.key.nome:
            root.right = self._delete_rec(root.right, nome)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._min_value_node(root.right)
            root.key = temp.key
            root.right = self._delete_rec(root.right, temp.key.nome)
        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current