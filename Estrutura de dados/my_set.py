# Estrutura de Dados: Conjunto (Set)
# 
# Um conjunto é uma coleção de elementos únicos, ou seja, não permite repetição.
# É útil para verificar se um item existe ou remover duplicatas.
# Este exemplo implementa um conjunto simples com métodos para adicionar, remover,
# verificar existência e exibir os elementos.

class MeuConjunto:
    def __init__(self):
        self.elementos = []

    def adicionar(self, elemento):
        if elemento not in self.elementos:
            self.elementos.append(elemento)

    def remover(self, elemento):
        if elemento in self.elementos:
            self.elementos.remove(elemento)

    def contem(self, elemento):
        return elemento in self.elementos

    def exibir(self):
        print(self.elementos)
