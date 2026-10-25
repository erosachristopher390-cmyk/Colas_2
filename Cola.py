from abc import ABC, abstractmethod


class Order:
    def __init__(self, qtty, customer):
        self._customer = customer
        self._qtty = qtty

    def print(self):
        print("     Customer: " + self.get_customer())
        print("     Quantity: " + str(self.get_qtty()))
        print("     ------------")

    def get_qtty(self):
        return self._qtty

    def get_customer(self):
        return self._customer


class QueueInterface(ABC):
    @abstractmethod
    def size(self):
        """Devuelve el número de elementos de la cola."""

    @abstractmethod
    def is_empty(self):
        """True si la cola está vacía, False si no."""

    @abstractmethod
    def front(self):
        """Devuelve el primer elemento SIN eliminarlo. None si está vacía."""

    @abstractmethod
    def enqueue(self, info):
        """Añade un nuevo elemento al final de la cola."""

    @abstractmethod
    def dequeue(self):
        """Devuelve el primer elemento y lo ELIMINA. None si está vacía."""


class Node:
    def __init__(self, info):
        self._info = info    # objeto que guarda el nodo
        self._next = None    # siguiente nodo (None si es el último)

    def get_info(self):
        return self._info

    def set_info(self, info):
        self._info = info

    def get_next(self):
        return self._next

    def set_next(self, next_node):
        self._next = next_node


class Queue(QueueInterface):
    def __init__(self):
        self._top = None     # cabeza (por donde se extrae)
        self._tail = None    # último nodo (por donde se inserta)
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def front(self):
        if self.is_empty():
            return None
        return self._top.get_info()

    def enqueue(self, info):
        new_node = Node(info)
        if self.is_empty():
            self._top = new_node
        else:
            self._tail.set_next(new_node)
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        info = self._top.get_info()
        self._top = self._top.get_next()
        self._size -= 1
        if self._top is None:    # la cola quedó vacía
            self._tail = None
        return info

    def get_nth(self, pos):
        """Devuelve el n-ésimo elemento (1 = primero) sin borrarlo; None si pos no es válida."""
        if pos < 1 or pos > self._size:
            return None
        node = self._top
        for _ in range(pos - 1):
            node = node.get_next()
        return node.get_info()

    def print_info(self):
        print("********* QUEUE DUMP *********")
        print("   Size: " + str(self._size))
        node = self._top
        i = 1
        while node is not None:
            print("   ** Element " + str(i))
            node.get_info().print()
            node = node.get_next()
            i += 1
        print("******************************")


# ---------------------- TestQueue ----------------------
def main():
    queue = Queue()

    o1 = Order(20, "cust1")
    o2 = Order(30, "cust2")
    o3 = Order(40, "cust3")
    o4 = Order(50, "cust4")

    print(">>> Cola vacía")
    queue.print_info()

    for n, o in enumerate([o1, o2, o3, o4], start=1):
        print(f">>> enqueue o{n}")
        queue.enqueue(o)
        queue.print_info()

    print(">>> front (no elimina)")
    queue.front().print()
    queue.print_info()

    print(">>> getNth(3) con los 4 elementos")
    queue.get_nth(3).print()

    print(">>> dequeue")
    queue.dequeue().print()
    queue.print_info()

    print(f">>> get_nth(0) y get_nth(10) -> {queue.get_nth(0)} / {queue.get_nth(10)}")

    print(">>> Vaciando la cola")
    while not queue.is_empty():
        queue.dequeue()
    queue.print_info()
    print("dequeue en cola vacía ->", queue.dequeue())
    print("front en cola vacía ->", queue.front())


if __name__ == "__main__":
    main()
