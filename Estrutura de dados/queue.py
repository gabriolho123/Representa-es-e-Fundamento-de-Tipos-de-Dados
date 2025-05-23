# Estrutura de Dados: Fila (Queue)
#
# Uma fila é uma estrutura do tipo FIFO (First-In, First-Out),
# onde o primeiro elemento a entrar é o primeiro a sair.
# É muito usada em sistemas de atendimento, buffers e processamento sequencial.
# Este exemplo implementa uma fila com métodos para enfileirar, desenfileirar
# e verificar se está vazia.

As listas são estruturas de dados que armazenam vários valores em uma única variável. Elas permitem acesso, modificação e ordenação de elementos.
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def size(self):
        return len(self.items)
