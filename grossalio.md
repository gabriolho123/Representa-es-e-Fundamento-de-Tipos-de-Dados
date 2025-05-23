Glossário Técnico – Tipos Primitivos e Abstratos de Dados
Prof Vinicius Costa Amador, Algoritmos e Lógica de Programação
Analise e Desenvolvimento de Sistemas, Turma E02
 
 
Tipo de dado – Conceito:
 
É uma forma de classificar os dados que um programa pode usar, como números, textos ou valores verdadeiros/falsos. Ele diz ao computador que tipo de informação está sendo usada.
 
Exemplo:
​•​idade = 25 → tipo inteiro
​•​nome = "Ana" → tipo texto (string)
​•​ativo = True → tipo verdadeiro/falso (booleano)
 
Tipos Primitivos
 
Tipos Primitivos – Conceito:
São os tipos de dados mais básicos e fundamentais que uma linguagem de programação oferece. Eles representam valores simples, como números e caracteres, e são usados como base para criar tipos mais complexos.
 
Exemplo:
•​idade = 30 → tipo inteiro (int)
•​peso = 70.5 → tipo ponto flutuante (float)
•​letra = ‘A’ → tipo caractere (char)
•​ativo = False → tipo verdadeiro/falso (booleano)
 
Inteiro (int) – Conceito:
É um tipo primitivo que representa números inteiros, positivos ou negativos, sem parte decimal. É usado para contar ou realizar operações matemáticas exatas.
 
Exemplo:
•​ano = 2025 → tipo inteiro
•​quantidade = -10 → tipo inteiro
 
Ponto flutuante (float/double) – Conceito:
É um tipo primitivo que representa números reais, ou seja, com parte decimal. É usado quando há necessidade de representar valores fracionários ou realizar cálculos com precisão decimal.
 
Exemplo:
•​altura = 1.75 → tipo ponto flutuante (float)
•​temperatura = -3.6 → tipo ponto flutuante (double)
 
Caractere (char) – Conceito:
É um tipo primitivo que representa um único símbolo, como uma letra, número ou sinal. É sempre armazenado entre aspas simples e usado para manipular textos em nível de caractere.
 
Exemplo:
•​letra = ‘B’ → tipo caractere
•​sinal = ‘?’ → tipo caractere
 
Booleano – Conceito:
É um tipo primitivo que representa apenas dois valores possíveis: verdadeiro ou falso. É usado para controlar decisões lógicas e fluxos de execução em programas.
 
Exemplo:
•​logado = True → tipo booleano
•​pagamento_realizado = False → tipo booleano
 
Tipo Abstrato de Dados
 
Tipo Abstrato de Dados – Conceito:
É um modelo lógico que define um conjunto de dados e as operações possíveis sobre eles, sem se preocupar com a implementação. Ele organiza dados de forma estruturada para resolver problemas específicos.
 
Exemplo:
•​pilha → estrutura onde o último elemento inserido é o primeiro a ser removido (LIFO)
•​fila → estrutura onde o primeiro elemento inserido é o primeiro a ser removido (FIFO)
 
Pilha (stack) – Conceito:
É um tipo abstrato de dado onde os elementos são inseridos e removidos pelo topo, seguindo a ordem LIFO (Last In, First Out – o último que entra é o primeiro que sai). É usada em situações como desfazer ações ou chamadas de funções.
 
Exemplo:
•​pilha.push(10) → adiciona 10 no topo
•​pilha.pop() → remove o elemento do topo (último inserido)
 
Fila (queue) – Conceito:
É um tipo abstrato de dado onde os elementos são inseridos no final e removidos do início, seguindo a ordem FIFO (First In, First Out – o primeiro que entra é o primeiro que sai). É usada para gerenciar tarefas em ordem de chegada.
 
Exemplo:
•​fila.enqueue(“João”) → adiciona “João” no final
•​fila.dequeue() → remove o primeiro elemento (“João”)
 
Lista (list) – Conceito:
É um tipo abstrato de dado que armazena uma sequência ordenada de elementos, que podem ser acessados por posições (índices). Permite inserções, remoções e buscas em diferentes partes da estrutura.
 
Exemplo:
•​lista = [10, 20, 30] → cria uma lista com três elementos
•​lista.append(40) → adiciona o valor 40 ao final da lista
 
Lista Encadeada (linked list) – Conceito:
É um tipo abstrato de dado onde cada elemento (nó) armazena um valor e uma referência (ponteiro) para o próximo nó da sequência. Permite inserções e remoções eficientes, principalmente no início ou meio da estrutura.
 
Exemplo:
•​nó1 → valor: 5, próximo: nó2
•​nó2 → valor: 10, próximo: nó3
•​nó3 → valor: 15, próximo: None
 
Operações Abstratas – Conceito:
São ações definidas para manipular tipos abstratos de dados, especificando o que pode ser feito sem detalhar como. Elas garantem que os dados sejam usados corretamente, como inserir, remover ou acessar elementos.
 
Exemplo:
•​inserir(elemento) → adiciona um item na estrutura
•​remover() → retira um item da estrutura
•​acessar(posição) → obtém o item em uma posição específica
 
Encapsulamento – Conceito:
É um princípio da programação que consiste em esconder os detalhes internos de um tipo de dado ou objeto, permitindo acesso somente por meio de métodos específicos. Isso protege os dados contra modificações indevidas.
 
Exemplo:
•​usar métodos como getIdade() e setIdade() para acessar ou alterar um atributo privado idade
•​bloquear o acesso direto a variáveis internas da classe
