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
        self.vida -= valor
        print(f"Tomou {valor} de dano. Vida atual: {self.vida}")
        
        if self.vida <= valor:
            self.morrer()


    def atacar(self,valor):
        self.vida -= valor

    def curar(self,valor):
        self.vida += valor

    def morrer(self, valor):
        valor >= self.vida
        print("Dead!")

    def usar_habilidade(self):
        print(f"A habilidade {random.choice(self.habilidades)} foi usada.")
        # print(f"{self.nome} usou a habilidade {random.choice(self.habilidades)}.")

    def rolar_iniciativa(self):
        print(f"Valor iniciativa: {random.randint(1,20)}.")


if __name__ == "__main__":
    personagem = Sistemas(["gelo", "fogo", "raio", "cura"])
    personagem.tomar_dano(5)
    personagem.atacar(10)
    personagem.curar(15)
    personagem.morrer(20)
    personagem.usar_habilidade()
    personagem.rolar_iniciativa()