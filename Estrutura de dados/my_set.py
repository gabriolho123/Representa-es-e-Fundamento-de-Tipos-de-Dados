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
