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
    def usar_habilidade(self, habilidades, alvo=None):
        pass

    @abstractmethod
    def rolar_iniciativa(self):
        pass


class Sistema(Entidade):

    # habilidades = {
    #     "fogo": {
    #         "tipo": "dano",
    #         "valor": 20
    #     },
    #     "gelo": {
    #         "tipo": "dano",
    #         "valor": 15
    #     },
    #     "raio": {
    #         "tipo": "dano",
    #         "valor": 25
    #     },
    #     "cura": {
    #         "tipo": "cura",
    #         "valor": 20
    #     },
    #     "nevoa": {
    #         "tipo": "dano",
    #         "valor": 15
    #     },
    #     "acido": {
    #         "tipo": "dano",
    #         "valor": 20
    #     },
    #     "lama": {
    #         "tipo": "dano",
    #         "valor": 10
    #     },
    #     "veneno": {
    #         "tipo": "dano",
    #         "valor": 25
    #     },
        
    # }

    def __init__(self, nome, tipo, habilidades=None, vida=100):
        self.nome = nome
        self.tipo = tipo
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

class Habilidades:

    def usar_habilidade(self, habilidade, atacante, alvo):
            
            if atacante == self.personagem:
            
                if habilidade in ('gelo', 'fogo'):
                    alvo.vida -= 15
                    
                elif habilidade == 'raio':
                    alvo.vida -= 25
                    
                elif habilidade == 'cura':
                    atacante.vida += 10
                    
            elif atacante == self.inimigo:
                
                if habilidade == 'névoa':
                    alvo.vida -= 15
                    
                elif habilidade in ('ácido', 'veneno'):
                    alvo.vida -= 20
                    
                elif habilidade == 'lama':
                    alvo.vida -= 10
        
        

    def rolar_iniciativa(self):
        iniciativa = random.randint(1, 20)

        print(
            f"{self.nome} rolou "
            f"{iniciativa} de iniciativa."
        )

        return iniciativa


if __name__ == "__main__":

    personagem = Sistema(
        nome="Mago",
        vida=190,
        habilidades=["fogo", "gelo", "raio", "cura"]
    )

    inimigo = Sistema(
        nome="Orc",
        vida=120,
        habilidades=["nevoa","acido","lama","veneno"]
    )

    personagem.rolar_iniciativa()
    inimigo.rolar_iniciativa()
    personagem.atacar(inimigo,20)
    inimigo.atacar(personagem,15)
    personagem.usar_habilidade("curar", inimigo)
    inimigo.usar_habilidade("veneno", personagem)



# if habilidade not in self.habilidades:
#             print(
#                 f"{self.nome} não possui a habilidade "
#                 f"'{habilidade}'."
#             )
#             return

#         dados = self.habilidades.get(habilidade)

#         if not dados:
#             print("Habilidade não cadastrada.")
#             return

#         if dados["tipo"] == "dano":

#             if alvo is None:
#                 print("Esta habilidade precisa de um alvo.")
#                 return

#             print(
#                 f"{self.nome} usou {habilidade} "
#                 f"em {alvo.nome}!"
#             )

#             alvo.tomar_dano(dados["valor"])

#         elif dados["tipo"] == "cura":

#             print(f"{self.nome} usou {habilidade}!")
#             self.curar(dados["valor"])