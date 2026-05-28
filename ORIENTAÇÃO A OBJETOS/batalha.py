import time
import random
import json
from entidade import Sistemas
from personagem import Personagem
from inimigo import Inimigo
from abc import ABC, abstractmethod

# class Batalha(ABC):
    
    # @abstractmethod
    # def rolar_iniciativa(self,valor):
    #     pass
    
    # @abstractmethod
    # def turnos(self,valor):
    #     pass
    
    # @abstractmethod
    # def personagem(self,valor):
    #     pass
    
    # @abstractmethod
    # def inimigo(self,valor):
    #     pass
    
    # @abstractmethod
    # def vez_turno(self,valor):
    #     pass
    
class BatalhaIniciar(Inimigo, Personagem):
    
    def __init__ (self, rodada, personagem: Personagem, inimigo: Inimigo):
        self.rodada = rodada
        self.personagem = personagem
        self.inimigo = inimigo
                  
      
    def iniciar(self):
        
        while True:
            resultado1 = random.randint(1, 10)
            print(f"{personagem.nome}, tirou o valor de iniciativa: {resultado1}.")
            
            resultado2 = random.randint(1,10)
            print(f"{inimigo.nome}, tirou o valor de iniciativa: {resultado2}.")
            
            if resultado1 > resultado2:
                print(f"{personagem.nome} inicia a rodada.")
                break
        
            elif resultado1 < resultado2:
                print(f"{inimigo.nome} inicia a rodada.")
                break
            
            else:
                print("Empate!")
                return
                  
        
    def turno(self):
        print(f"Rodada {self.rodada}.")
        self.rodada =+ 1
        
        while self.personagem.vida > 0 or self.inimigo.vida > 0:
            print("1 - Atacar.")
            print("2 - Curar.")
            print("3 - Usar habilidade.")
            print("4 - Passar rodada.")
            
            escolha = input("Escolha um valor: ")
            if escolha == "1":
                self.personagem.atacar(self.inimigo, 10)
                
            if escolha == "2":
                self.personagem.curar(5)
                
            if escolha == "3":
                self.personagem.usar_habilidade()
                
   
            
            
        
        
        
        
        
if __name__ == "__main__":
    inimigo = Inimigo("Morun", 160, ["ogro","orc","dríade", "goblin"], ["gelo", "fogo", "raio", "cura"])
    personagem = Personagem("Nami", 200, 2, ["gelo", "fogo", "raio", "cura"], False) 
    batalha = BatalhaIniciar(1, personagem, inimigo)
    batalha.iniciar()
    batalha.turno()
    batalha.atacar()

