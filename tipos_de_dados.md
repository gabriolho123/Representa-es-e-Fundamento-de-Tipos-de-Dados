
# Tipos Primitivos de Dados e Estruturas de Dados

## 📌 Conceitos Básicos

### Algoritmo
Uma sequência finita de ações (raciocínios, instruções ou operações) para resolver um problema.
- Ex: Receita de bolo, cálculo de média.

### Variável
Espaço na memória para armazenar dados.
- Ex: Nome, idade, altura, peso.

## 🎯 Tipos Primitivos de Dados

| Tipo    | Descrição                                       | Exemplos                                |
|---------|--------------------------------------------------|------------------------------------------|
| Inteiro | Números sem casas decimais                      | `1`, `-3`, `+10`, `idade`, `pontuação`   |
| Real    | Números com casas decimais                      | `3.14`, `-6.0`, `peso`, `altura`         |
| Lógico  | Valores booleanos (Verdadeiro ou Falso)         | `True`, `False`, `ligado`, `autenticado` |
| Texto   | Sequência de caracteres                         | `"nome"`, `"email"`, `"cidade"`          |

### Exemplos em Linguagens:

**Java**
- `byte`, `short`, `int`, `long`

**Python**
- `int`, `float`, `bool`, `str`

## 🧠 Exemplos Práticos

- `int quantidadeEmEstoque = 150;` (controle de estoque)
- `double precoDoPedido = 29.90;` (app delivery)
- `char genero = 'M';` (cadastro)
- `boolean estaLogado = true;` (login)

---

## 🔷 Classes Abstratas

Classes que **não podem ser instanciadas** diretamente, servem como **modelo base**.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

cachorro = Cachorro()
cachorro.emitir_som()  # Saída: Au au!
```

### Características
- Contêm métodos **abstratos** (sem implementação)
- Podem ter métodos **concretos**
- **Usadas com herança**: obrigam subclasses a implementarem métodos

---

## 📚 TDAs – Tipos Abstratos de Dados

### 1. Lineares
- **Lista** (List / Array)
- **Tupla** (Tuple)
- **Pilha** (Stack) – LIFO
- **Fila** (Queue) – FIFO
- **Deque** – Inserção/rem. nas duas pontas

### 2. Não Lineares
- **Árvore** (Tree, AVL, B-Tree)
- **Heap** (MinHeap / MaxHeap)
- **Grafo** (Graph)
- **Trie** – Árvore de Prefixos

### 3. Associativos (Chave-Valor)
- **Dicionário** (Map / HashMap)
- **Tabela Hash**
- **Objeto** – via classes

### 4. Conjuntos
- **Set**
- **Multiset**
- **Bitset / Bitmap**

### 5. Compostos / Estruturados
- **Matriz (Grid)**
- **Matriz Esparsa**
- **Buffer Circular**

### 6. Avançados
- **Fila de Prioridade**
- **Disjoint Set (Union-Find)**
- **Bloom Filter**
- **Autômato Finito**

---

## 🧪 Quando usar classes abstratas?

- Quando você **quer garantir** que todas as subclasses implementem certos métodos.
- Para **padronizar comportamentos** em hierarquias de classes.
