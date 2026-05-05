class Personagem:
    # [] habilidades
    # subir de nível
    # sair da guilda
    # usar habilidade


    def __int__(self, nome, nivel, genero, guilda):
        self.nome = nome
        self.nivel = nivel
        self.genero = genero
        self.guilda = guilda


    def __str__(self):
        return f"Esse é {self.nome}, um personagem de nível {self.nivel}, do gênero {self.genero}, está na guilda {self.guilda}"
    
    def entrar_guilda(self, nome_guilda):
        self.guilda = True
        print(f"{self.nome} entrou para a {nome_guilda}")



    Personagem = ("Nami", 2, "Feminino", False)