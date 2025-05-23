# Estrutura de Dados: Array Dinâmico (Dynamic Array)
#
# Um array dinâmico é como uma lista comum em Python,
# mas com gerenciamento interno de capacidade.
# Ele permite crescer automaticamente quando mais espaço é necessário.
# Este exemplo simula o comportamento de um array dinâmico com métodos para
# adicionar, remover e acessar elementos.

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
