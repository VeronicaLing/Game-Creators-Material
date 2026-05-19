from abc import ABC, abstractmethod
import random

class Entidade(ABC):


    @abstractmethod
    def tomar_dano(self,valor):
        pass

    @abstractmethod
    def atacar(self,valor):
        pass

    @abstractmethod
    def curar(self,valor):
        pass

    @abstractmethod
    def morrer(self,valor):
        pass

    @abstractmethod
    def usar_habilidade(self,habilidade):
        pass

    @abstractmethod
    def rolar_iniciativa(self,valor):
        pass


class Sistemas(Entidade):

    def __init__(self, habilidades=None, vida=100):
        self.habilidades = habilidades 
        self.vida = vida

    def tomar_dano(self, valor):
        if self.vida <= valor:
            self.morrer()

        self.vida -= valor

    def atacar(self,valor):
        self.vida -= valor

    def curar(self,valor):
        self.vida += valor

    def morrer(self):
        print("dead")

    def usar_habilidade(self, habilidade):
        if habilidade in self.usar_habilidade:
            print(f"{habilidade} foi usada!")

    def rolar_iniciativa(self):
        print(f"{random.choice(1-20)}")



personagem = Sistemas(["gelo", "fogo", "raio", "cura"])
personagem.tomar_dano(5)
personagem.atacar(10)
personagem.curar(15)
personagem.morrer()
# personagem.usar_habilidade()
personagem.rolar_iniciativa()