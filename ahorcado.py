import random


class juegoAhorcado:
    estados = [
        r"""
         +--+
         |  |
            |
            |
            |
            |
        =====""",
        r"""
         +--+
         |  |
         O  |
            |
            |
            |
        =====""",
        r"""
         +--+
         |  |
         O  |
         |  |
            |
            |
        =====""",
        r"""
         +--+
         |  |
         O  |
        /|  |
            |
            |
        =====""",
        r"""
         +--+
         |  |
         O  |
        /|\ |
            |
            |
        =====""",
        r"""
         +--+
         |  |
         O  |
        /|\ |
        /   |
            |
        =====""",
        r"""
         +--+
         |  |
         O  |
        /|\ |
        / \ |
            |
        ====="""]

    salvado = [
        r"""
         +--+
            |
            |
        \O/ |
         |  |
        / \ |
        ====="""]

    categorias = 'FRUTAS JUEGOS PELICULAS'.split()
    palabrasFrutas = 'PERA PLATANO UVA MANZANA MELOCOTON KIWI ALBARICOQUE CEREZA CIRUELA FRESA GRANADA HIGO LIMA LIMON MANDARINA NARANJA MELON MORA NISPERO PIÑA POMELO SANDIA '.split()
    palabrasJuegos = 'MONOPOLY SCRABBLE AJEDREZ RISK UNO STRATEGO PICTIONARY'.split()
    palabrasPeliculas = 'INTERSTELLAR PARASITOS CARS CREEME VIKINGOS'.split()
    categoriaElegida = random.choice(categorias)

    def jugarAhorcado(self):

        letrasIncorrectas = []
        letrasCorrectas = []
        palabraSecreta = random.choice(self.palabrasFrutas)
        nombreJugador = input("Dime el nombre del jugador: ")

        palabraSecreta = None
        if self.categoriaElegida == "FRUTAS":
            palabraSecreta = random.choice(self.palabrasFrutas)

        elif self.categoriaElegida == "JUEGOS":
            palabraSecreta = random.choice(self.palabrasJuegos)

        elif self.categoriaElegida == "PELICULAS":
            palabraSecreta = random.choice(self.palabrasPeliculas)

        while True:
            self.dibujar(letrasIncorrectas, letrasCorrectas, palabraSecreta)

            numeroLetras = self.dimeLetra(letrasIncorrectas + letrasCorrectas)

            if numeroLetras in palabraSecreta:

                letrasCorrectas.append(numeroLetras)

                ganarPartida = True
                for letrasSecretas in palabraSecreta:
                    if letrasSecretas not in letrasCorrectas:
                        ganarPartida = False
                        break
                if ganarPartida:
                    print(self.salvado[0])
                    print('¡Bien hecho! la palabra secreta es :', palabraSecreta)
                    print('Has ganado! ' + str(nombreJugador))
                    break

            else:
                letrasIncorrectas.append(numeroLetras)

                if len(letrasIncorrectas) == len(self.estados) - 1:
                    self.dibujar(letrasIncorrectas, letrasCorrectas, palabraSecreta)
                    print('Demasiados intentos!')
                    print('La palabra era "{}"'.format(palabraSecreta))
                    break

    def dibujar(self, letrasIncorrectas, letrasCorrectas, palabraSecreta):
        print(self.estados[len(letrasIncorrectas)])
        print('La categoría es: ', self.categoriaElegida)
        print()
        print('Intentos restantes:', self.numIntentosRestantes(letrasIncorrectas))
        print('Letras incorrectas: ', end='')
        for letras in letrasIncorrectas:
            print(letras, end=' ')
        if len(letrasIncorrectas) == 0:
            print('No hay letras incorrectas.')
        elif len(letrasIncorrectas) == len(letrasIncorrectas) + 1:
            print('Letras diferentes.')
        elif len(letrasIncorrectas) == len(letrasIncorrectas) + 2:
            print('No coinciden.')

        print()

        espaciosLetras = ['_'] * len(palabraSecreta)

        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] in letrasCorrectas:
                espaciosLetras[i] = palabraSecreta[i]

        print(' '.join(espaciosLetras))

    def dimeLetra(self, letrasElegidas):
        while True:
            print('Adivina una letra o escribe "TERMINAR" para finalizar la partida.')
            adivina = input('> ').upper()
            if adivina == "TERMINAR":
                print(self.estados[6])
                print('La partida ha sido terminada.')
                break
            if len(adivina) != 1:
                print('Introduce una única letra.')
            elif adivina in letrasElegidas:
                print('Esa letra ya la sabías. Elige otra vez.')
            elif not adivina.isalpha():
                print('Introduce una LETRA.')

            else:
                return adivina

    def numIntentosRestantes(self, intentsIncorrectes):
        return (len(self.estados) - len(intentsIncorrectes) - 1)


if __name__ == '__main__':
    juego1 = juegoAhorcado()
    juego1.jugarAhorcado()
