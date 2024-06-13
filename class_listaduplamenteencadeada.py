class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, tarefa):
        new_node = NodeDoublyCircular(tarefa)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def remove(self, tarefa):
        if not self.head:
            return
        current = self.head
        while True:
            if current.data == tarefa:
                if current.next == current:  # único nó na lista
                    self.head = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    if current == self.head:
                        self.head = current.next
                return
            current = current.next
            if current == self.head:
                break

    def traverse(self):
        result = []
        if not self.head:
            return result
        current = self.head
        while True:
            result.append(current.data)
            current = current.next
            if current == self.head:
                break
        return result
class NodeDoublyCircular:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None