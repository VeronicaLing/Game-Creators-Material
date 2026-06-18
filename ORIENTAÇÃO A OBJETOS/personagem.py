import time
import random
import json
from entidade2 import Sistema

class Personagem(Sistema):
        
    def __init__(self, nome, vida, nivel=0, habilidades=None, guilda=False):
        self.nome = nome
        self.vida = vida
        self.nivel = nivel
        self.habilidades = habilidades 
        self.guilda = guilda

    def __str__(self):
        return f"Esse(a) é {self.nome}, um personagem de nível {self.nivel}, que está na guilda {self.guilda}."
    
    def entrar_guilda(self, nome_guilda):
        self.guilda = True
        print(f"{self.nome} entrou para a {nome_guilda}.")

    def sair_guilda(self, nome_guilda):
        self.guilda = False
        print(f"{self.nome} saiu da guilda {nome_guilda}.")

    def subir_de_nível(self, valor:int):
        self.nivel += valor
        print(f"{self.nome} subiu para o nível {self.nivel}!")

    # def usar_habilidade(self):
    #     print(f"{self.nome} usou a habilidade {random.choice(self.habilidades)}.")

    def usar_habilidade(self, habilidade, alvo):
        if alvo == self:
            print(f"{self.nome} usou {habilidade}! Vida atual: {self.vida}.")
        else:
            print(f"{self.nome} usou {habilidade}!\n{alvo.nome} vida atual: {alvo.vida}.")
            
        
    def rolar_iniciativa(self):
        iniciativa = random.randint(1, 20)
        print(f"{self.nome} rolou {iniciativa}.")
        return iniciativa


    def salvar_dados(self):

        personagem = {
            "nome": self.nome,
            "nivel": self.nivel,
            "habilidades": self.habilidades,
            "guilda": self.guilda,
        }

        with open ("aula_01.json", "w") as arquivo:
            json.dump(personagem, arquivo)


    def importar_dados(self):
        with open ("aula_01.json", "r") as arquivo:
            print(json.load(arquivo))



if __name__ == "__main__":
    personagem = Personagem("Nami", 150, 2, ["gelo", "fogo", "raio", "cura"], False)
    print(personagem)
    personagem.entrar_guilda("Houth")
    personagem.sair_guilda("Houth")
    personagem.subir_de_nível(1)
    personagem.usar_habilidade()
    personagem.salvar_dados()
    personagem.importar_dados()
