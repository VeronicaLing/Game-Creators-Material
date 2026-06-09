import random
import time

class Habilidade:
    
    
    def __init__(self, nome, tipo, valor):
        self.nome = nome
        self.tipo = tipo
        self.valor =  valor
        
        
    def usar_habilidade(self, alvo, habilidade):
        if habilidade.tipo == "dano":
            alvo.tomar_dano(habilidade.valor)
        elif habilidade.tipo == "cura":
            alvo.curar(habilidade.valor)
        elif habilidade.tipo == "buff":
            alvo.buff(habilidade.valor)
            


class P:
    def __init__(self, nome, vida, habilidades=None):
        self.nome = nome
        self.vida = vida
        self.habilidades = habilidades or None
        
    def tomar_dano(self, dano):
        self.vida -= dano
        print(f"{self.nome} tomou {dano} de dano \nVida restante: {self.vida}")
        
    def curar(self, valor):
        self.vida += valor
        print(f"Vida Atual: {self.vida}")
    
    
    def ganhar_habilidade(self, nome, tipo, valor):
        
        nh = Habilidade(nome, tipo, valor)
        self.habilidades.append(nh)

        print(self.habilidades)
        
    def atacar(self, alvo):
        e = input("Deseja atacar(1) ou usar habilidade(2)? ")
        
        if e == "1":
            print(f"{self.nome} está atacando {alvo.nome}!")
            time.sleep(0.3)
            alvo.tomar_dano(5)
        elif e == "2":
            hab = random.choice(self.habilidades)
            print(f"{self.nome} vai usar a habilidade {hab.nome}... \nEla é do tipo: {hab.tipo}!")
            e = input("Qual o alvo? Inimigo(1) ou Personagem(2): ")
            if e == "1":
                time.sleep(0.3)
                hab.usar_habilidade(alvo, hab)
            elif e == "2":
                time.sleep(0.3)
                hab.usar_habilidade(self, hab)
                    
            
        

if __name__ == "__main__":
    bf = Habilidade("bola de fogo", "dano", 10)
    bg = Habilidade("bola de gelo", "dano", 5)
    bc = Habilidade("bola de cura", "cura", 8)
    
    pers = P("Carlos", 20, [bf, bg, bc])
    pers2 = P("Danny", 40, [bc])
    
    pers.ganhar_habilidade("bola de trevas", "dano", 2)
    
    while True:
        pers.atacar(pers2)