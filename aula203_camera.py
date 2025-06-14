

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f"Essa bagaça {self.nome} esta dendo filmada...")

        print(f"O {self.nome} esta filmando a bagaça...")
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f"Essa bagaça {self.nome} não esta filmando...")

        print(f"O {self.nome} esta parando de filmar...")
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar em quanto filma!!!')
            return
        
        print(f'A {self.nome} Esta Fotografando essa bagunça>>>!!!')

c1 = Camera('Canon')
c2 = Camera('Sony')
c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()
