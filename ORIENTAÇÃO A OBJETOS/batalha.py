import time
import random
import json
from entidade import Sistemas
from personagem import Personagem
from inimigo import Inimigo
from abc import ABC, abstractmethod

    
class BatalhaIniciar:
    
    def __init__ (self, rodada, personagem: Personagem, inimigo: Inimigo):
        self.rodada = rodada
        self.personagem = personagem
        self.inimigo = inimigo
                  
      
    def iniciar(self, atacante, alvo):
        
        iniciativa = random.randint(1, 20)
        
        turno = iniciativa > 10
        # print(f"Valor de iniciativa: {iniciativa}.")
        
        rodada = 1
        while alvo.vida > 0 or atacante.vida > 0:
            print(f"Rodada {rodada}.")
            
            if turno:
                print(f"Rodada de {atacante.nome}.")
                self.evento(personagem, inimigo)
                
        
            elif not turno:
                print(f"{alvo.nome} inicia a rodada.")
                self.evento(inimigo, personagem)
                
            turno = not turno
            rodada += 1
            
    def evento(self, atacante, alvo):    
                  
        print("1 - Atacar.")
        print("2 - Curar.")
        print("3 - Usar habilidade.")
        print("4 - Passar rodada.")
        
        escolha = input("Escolha um valor: ")
        if escolha == "1":
            atacante.atacar(alvo, 10)
            
        elif escolha == "2":
            atacante.curar(5)
            
        elif escolha == "3":
            atacante.usar_habilidade()
            
        elif escolha == "4":
            pass

            
   
        
if __name__ == "__main__":
    inimigo = Inimigo("Morun", 160, ["ogro","orc","dríade", "goblin"], ["gelo", "fogo", "raio", "cura"])
    personagem = Personagem("Nami", 200, 2, ["gelo", "fogo", "raio", "cura"], False) 
    batalha = BatalhaIniciar(1, personagem, inimigo)
    batalha.iniciar(personagem, inimigo)


#def iniciar(self):
        
#         while True:
#             resultado1 = random.randint(1, 10)
#             print(f"{personagem.nome}, tirou o valor de iniciativa: {resultado1}.")
            
#             resultado2 = random.randint(1,10)
#             print(f"{inimigo.nome}, tirou o valor de iniciativa: {resultado2}.")
            
#             if resultado1 > resultado2:
#                 print(f"{personagem.nome} inicia a rodada.")
#                 personagem == "atacante"
#                 self.turno(personagem, inimigo)
        
#             elif resultado1 < resultado2:
#                 print(f"{inimigo.nome} inicia a rodada.")
#                 inimigo == "alvo"
#                 self.turno(inimigo, personagem)
#                 break
            
#             else:
#                 print("Empate!")
                
                  
#     def turno(self, atacante, alvo):
#         rodada = 1
        
#         while alvo.vida > 0 or atacante.vida > 0:
#             print(f"Rodada {rodada}.")
#             print("1 - Atacar.")
#             print("2 - Curar.")
#             print("3 - Usar habilidade.")
#             print("4 - Passar rodada.")
            
#             escolha = input("Escolha um valor: ")
#             rodada += 1
#             if escolha == "1":
#                 atacante.atacar(alvo, 10)
                
#             elif escolha == "2":
#                 atacante.curar(5)
                
#             elif escolha == "3":
#                 atacante.usar_habilidade()
                
#             elif escolha == "4":
#                 pass