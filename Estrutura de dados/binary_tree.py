# Estrutura de Dados: Árvore Binária (Binary Tree)
#
# Uma árvore binária é uma estrutura hierárquica onde cada nó tem
# no máximo dois filhos: esquerdo e direito.
# É útil para busca, ordenação e organização de dados.
# Este exemplo implementa uma árvore binária básica com inserção e travessia
# em ordem (in-order traversal).

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = Node(valor)
        else:
            self._inserir_recursivo(valor, self.raiz)

    def _inserir_recursivo(self, valor, no_atual):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = Node(valor)
            else:
                self._inserir_recursivo(valor, no_atual.esquerda)
        else:
            if no_atual.direita is None:
                no_atual.direita = Node(valor)
            else:
                self._inserir_recursivo(valor, no_atual.direita)

    def em_ordem(self, no=None):
        if no is None:
            no = self.raiz
        if no:
            self.em_ordem(no.esquerda)
            print(no.valor, end=' ')
            self.em_ordem(no.direita)
