class Juego:
    def __init__(self):
        lista1 = []
        lista2 = []
        self.diccionarioLimite = []
        self.diccionarioLimite.append(lista1)
        self.diccionarioLimite.append(lista2)
        self.tablero = crearTableroVacio()
        self.agrupacionesJugador = []
        self.agrupacionesJugador.append([])
        self.agrupacionesJugador.insert(1, lista1)
        self.agrupacionesJugador.insert(2, lista2)

    def colocarPieza(self, coord, turno):
        "Coloca en la posicion coord el valor turno"
        encontreEmparejamiento = False
        i = 0
        if( not self.diccionarioLimite[turno] or self.diccionarioLimite[turno][coord] ==  None):
            self.tablero[coord.f][coord.c]  == turno
            agrupacion = Agrupacion()
            agrupacion.puntos.append(coord)
            # recorrida horizontal
            if(coord.f!=0):
                agrupacion.limites.append(Limite(Coord(coord.f+pow(-1,i),coord.c+pow(-1,j)),self.tablero[coord.f][coord.c]!= 0))
        self.tablero[coord.f][coord.c] = turno
        self.agrupacionesJugador[turno]
        return
    def printTablero(self):
        "muestra el tablero actual"
        str1  = " XX | 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 \n"
        str1 += "------------------------------------------------------------------\n"
        for i in range(15):
            for j in range(15):
                if(j == 0):
                    if(i>=10):
                        str1 += " "+ str(i) + " |"
                    else:
                        str1 += " 0"+ str(i) + " |"
                str1 += "  "+str(self.tablero[i][j])
                if(j==14):
                    str1 += "\n"
        print(str1)
def crearTableroVacio():
    "Crea el tablero vacío"
    tablero = []
    for i in range(15):
        linea = []
        for j in range(15):
            linea.append(0)
        tablero.append(linea)
    return tablero


def valorar(tablero, turno):
    "Valora el tablero para cada jugador"
    return


def formaciones(tablero, turno):
    "Devuelte las formaciones que aun me sirven"
    return


class Coord:
    def __init__(self, f, c):
        self.f = f
        self.c = c

    def strCoord(self):
        return '(' + str(self.f) + ',' + str(self.c) + ')'




class Agrupacion:
    def __init__(self):
        self.puntos= []
        self.limites = []

    def printForm(self):
        print('(' + self.inicio.strCoord() + ',' + self.fin.strCoord() + ')')

class Limite:
    def __init__(self, coord, rival):
        self.coord = coord
        self.rival =  rival

juego = Juego()
juego.colocarPieza(Coord(0, 1), 1)
juego.colocarPieza(Coord(0, 2), 1)
juego.colocarPieza(Coord(0, 3), 1)
juego.colocarPieza(Coord(1, 1), 1)
juego.colocarPieza(Coord(2, 1), 1)
juego.colocarPieza(Coord(3, 1), 1)
juego.printTablero()
agrupacioneshorizontales = juego.agrupacionesH(1)
agrupacionesverticales = juego.agrupacionesV(1)

juego.printagrupacionesH(1)

i = 1
