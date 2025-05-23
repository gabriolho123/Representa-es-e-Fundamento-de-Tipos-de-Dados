# Tipos Abstratos de Dados (TADs)
Classes abstratas são classes que não podem ser instanciadas diretamente e servem como modelo base para outras classes. Elas são usadas em programação orientada a objetos para definir uma estrutura comum que outras classes devem seguir.

Características principais:

Contêm métodos abstratos, que são métodos sem implementação (ou seja, apenas a assinatura).

Podem conter métodos concretos, ou seja, com implementação.

São usadas como base para herança: outras classes herdam e implementam os métodos abstratos.


1. TDAs Lineares
Estruturas com elementos organizados em sequência.

Lista (List / Array)

Tupla (Tuple)

Pilha (Stack) – LIFO

Fila (Queue) – FIFO

Deque (Double-Ended Queue) – Inserção e remoção em ambas as extremidades

2. TDAs Não Lineares
Estruturas com organização hierárquica ou em rede.

Árvore (Tree)

Ex: Árvore Binária, AVL, B-Tree

Heap (MinHeap / MaxHeap)

Grafo (Graph)

Trie (Árvore de Prefixos)

3. TDAs Associativos (Chave-Valor)
Permitem mapear dados por chaves.

Dicionário (Map / HashMap)

Tabela Hash (Hash Table)

Tabela de Símbolos (Symbol Table)

Registro / Struct / NamedTuple

Objeto (Object) – via classes

4. TDAs Conjuntos
Coleções não ordenadas, com controle de duplicatas.

Conjunto (Set)

Multiconjunto (Multiset / Bag) – permite repetições

Bitset / Bitmap – representação com bits

5. TDAs Estruturados / Compostos
Organizam dados em tabelas ou blocos multidimensionais.

Tabela / Matriz (Grid / Matrix)

Matriz Esparsa (Sparse Matrix)

Buffer Circular / Deque Circular

6. TDAs Avançados e Especializados
Usados em contextos técnicos, algoritmos ou sistemas de alta performance.

Fila de Prioridade (Priority Queue) – com heap

Disjoint Set (Union-Find) – conjuntos disjuntos

Bloom Filter – estrutura probabilística para verificação de pertencimento

Autômato Finito (Finite Automaton) – usado em reconhecimento de padrões

Fila com Prioridade Estável – mantém ordem de chegada com prioridades
