# Tipos Abstratos de Dados (TADs)
Classes abstratas são classes que não podem ser instanciadas diretamente e servem como modelo base para outras classes. Elas são usadas em programação orientada a objetos para definir uma estrutura comum que outras classes devem seguir.

Características principais:

Contêm métodos abstratos, que são métodos sem implementação (ou seja, apenas a assinatura).

Podem conter métodos concretos, ou seja, com implementação.

São usadas como base para herança: outras classes herdam e implementam os métodos abstratos.


Exemplo em Python:

from abc import ABC, abstractmethod

class Animal(ABC):  # classe abstrata

    @abstractmethod
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

# animal = Animal()  # Isso daria erro, não pode instanciar
cachorro = Cachorro()
cachorro.emitir_som()  # Saída: Au au!

Quando usar?

Quando você quer garantir que todas as subclasses implementem certos métodos.

Quando deseja padronizar comportamentos em uma hierarquia de classes.
