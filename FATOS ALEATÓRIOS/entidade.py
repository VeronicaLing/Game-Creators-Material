# from abc import ABC, abstractmethod
# import random

# class Entidade(ABC):

#     @abstractmethod
#     def tomar_dano(self,valor):
#         pass

#     @abstractmethod
#     def atacar(self,valor):
#         pass

#     @abstractmethod
#     def curar(self,valor):
#         pass

#     @abstractmethod
#     def morrer(self,valor):
#         pass

#     @abstractmethod
#     def usar_habilidade(self,habilidade):
#         pass

#     @abstractmethod
#     def rolar_iniciativa(self,valor):
#         pass


# class Sistemas(Entidade):

#     def __init__(self, habilidades=None, vida=100):
#         self.habilidades = habilidades
#         self.vida = vida

#     def tomar_dano(self, valor):
#         self.vida -= valor
#         print(f"Tomou {valor} de dano. Vida atual: {self.vida}")
        
#         if self.vida <= valor:
#             self.morrer()


#     def atacar(self, alvo, valor):
#         print(f"{alvo.nome} sofreu dano ")
#         alvo.tomar_dano(valor)

#     def curar(self,valor):
#         self.vida += valor
#         print(f"{self.nome} curou {valor}")

#     def morrer(self, valor):
#         valor >= self.vida
#         print("Dead!")

#     def usar_habilidade(self):
#         print(f"A habilidade {random.choice(self.habilidades)} foi usada.")

#     def rolar_iniciativa(self):
#         print(f"Valor iniciativa: {random.randint(1,20)}.")
     
        
# class Habilidades():
    
#     def __init__ (self, habilidade, personagem: Personagem, inimigo: Inimigo):
#         self.habilidade = habilidade
#         self.personagem = personagem
#         self.inimigo = inimigo
        
#     def usar_habilidade(self, habilidade, atacante, alvo):
        
#         if atacante == self.personagem:
        
#             if habilidade in ('gelo', 'fogo'):
#                 alvo.vida -= 15
                
#             elif habilidade == 'raio':
#                 alvo.vida -= 25
                
#             elif habilidade == 'cura':
#                 atacante.vida += 10
                
#         elif atacante == self.inimigo:
            
#             if habilidade == 'névoa':
#                 alvo.vida -= 15
                
#             elif habilidade in ('ácido', 'veneno'):
#                 alvo.vida -= 20
                
#             elif habilidade == 'lama':
#                 alvo.vida -= 10
            



from abc import ABC, abstractmethod
import random


class Entidade(ABC):

    @abstractmethod
    def tomar_dano(self, valor):
        pass

    @abstractmethod
    def atacar(self, alvo, valor):
        pass

    @abstractmethod
    def curar(self, valor):
        pass

    @abstractmethod
    def morrer(self):
        pass

    @abstractmethod
    def usar_habilidade(self, habilidade, alvo):
        pass

    @abstractmethod
    def rolar_iniciativa(self):
        pass


class Sistema(Entidade):

    def __init__(self, nome, habilidades=None, vida=100):
        self.nome = nome
        self.habilidades = habilidades or []
        self.vida = vida

    def tomar_dano(self, valor):
        self.vida -= valor

        print(
            f"{self.nome} recebeu {valor} de dano. "
            f"Vida atual: {self.vida}"
        )

        if self.vida <= 0:
            self.morrer()

    def atacar(self, alvo, valor):
        print(f"{self.nome} atacou {alvo.nome}!")
        alvo.tomar_dano(valor)

    def curar(self, valor):
        self.vida += valor

        print(
            f"{self.nome} recuperou {valor} pontos de vida. "
            f"Vida atual: {self.vida}"
        )

    def morrer(self):
        print(f"{self.nome} morreu!")

    def usar_habilidade(self, habilidade, alvo):
        Habilidades.usar_habilidade(habilidade, self, alvo)

    def rolar_iniciativa(self):
        iniciativa = random.randint(1, 20)
        print(f"{self.nome} rolou {iniciativa} de iniciativa.")
        return iniciativa




# class Habilidades:

#     def usar_habilidade(self, habilidade, atacante, alvo):
            
#             if atacante == self.personagem:
            
#                 if habilidade in ('gelo', 'fogo'):
#                     alvo.vida -= 15
                    
#                 elif habilidade == 'raio':
#                     alvo.vida -= 25
                    
#                 elif habilidade == 'cura':
#                     atacante.vida += 10
                    
#             elif atacante == self.inimigo:
                
#                 if habilidade == 'névoa':
#                     alvo.vida -= 15
                    
#                 elif habilidade in ('ácido', 'veneno'):
#                     alvo.vida -= 20
                    
#                 elif habilidade == 'lama':
#                     alvo.vida -= 10
                     
        


if __name__ == "__main__":
    personagem = Sistema(["gelo", "fogo", "raio", "cura"])
    personagem.tomar_dano(5)
    personagem.atacar(10)
    personagem.curar(15)
    personagem.morrer(20)
    personagem.usar_habilidade()
    personagem.rolar_iniciativa()