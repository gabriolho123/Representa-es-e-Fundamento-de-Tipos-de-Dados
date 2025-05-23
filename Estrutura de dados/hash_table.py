# Estrutura de Dados: Tabela Hash (Hash Table)
#
# Uma tabela hash é uma estrutura que armazena pares chave-valor.
# Utiliza uma função hash para mapear chaves a índices de forma eficiente.
# Muito usada para buscas rápidas, como dicionários em Python.
# Este exemplo implementa uma tabela hash simples com inserção, busca
# e remoção de elementos.


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def inserir(self, chave, valor):
        index = self._hash_function(chave)
        if self.table[index] is None:
            self.table[index] = []
        self.table[index].append((chave, valor))

    def buscar(self, chave):
        index = self._hash_function(chave)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == chave:
                    return v
        return None
