import time
import random
import json
from entidade import Sistema

class Inimigo(Sistema):
        
        
    def __init__(self, nome, vida, classe, habilidade=None, nivel=0):
        self.nome = nome
        self.nivel = nivel
        self.habilidade = habilidade
        self.vida = vida 
        self.classe = classe

    def __str__(self):
        return f"Esse(a) é {self.nome}, um monstro de nível {self.nivel}, da classe {random.choice(self.classe)}."
    
    def definir_nivel(self):
        if self.vida < 150:
            self.nivel=10
        elif self.vida in range (150,300):
            self.nivel=20
        else: self.nivel=30
        
        print(f"{self.nome} está no nível {self.nivel}.")
        
    
    def definir_classe(self):
        print(f"{self.nome} é da classe {random.choice(self.classe)}.")
        
    def habilidades(self):
        print(f"{self.nome} é usuário da habilidade {random.choice(self.habilidade)}.")


    def salvar_dados(self):

        inimigo = {
            "nome": self.nome,
            "nivel": self.nivel,
            "habilidades": self.habilidade,
            "claase": self.classe,
        }

        with open ("aula_01.json", "w") as arquivo:
            json.dump(inimigo, arquivo)


    def importar_dados(self):
        with open ("aula_01.json", "r") as arquivo:
            print(json.load(arquivo))


if __name__ == "__main__":
    inimigo = Inimigo("Morun", 160, ["ogro","orc","dríade", "goblin"], ["gelo", "fogo", "raio", "cura"])
    inimigo.habilidades()
    inimigo.definir_classe()
    inimigo.definir_nivel()
    # inimigo.salvar_dados()
    # inimigo.importar_dados()
    inimigo.tomar_dano(10)
    inimigo.curar(5)
