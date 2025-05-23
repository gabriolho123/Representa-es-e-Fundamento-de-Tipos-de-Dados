class ArrayDinamico:
    def __init__(self):
        self.array = []
    
    def adicionar(self, valor):
        self.array.append(valor)
    
    def remover(self, valor):
        if valor in self.array:
            self.array.remove(valor)
    
    def obter(self, indice):
        if 0 <= indice < len(self.array):
            return self.array[indice]
        return None
    
    def tamanho(self):
        return len(self.array)
