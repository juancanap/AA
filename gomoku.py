class Juego:
    agrupacionesJugador = []
    def __init__(self):
        self.tablero = crearTableroVacio()
        lista = []
        lista2 = []
        self.agrupacionesJugador = []
        self.agrupacionesJugador.append([])
        self.agrupacionesJugador.insert(1, lista)
        self.agrupacionesJugador.insert(2, lista2)

    def colocarPieza(self, coord, turno):
        "Coloca en la posicion coord el valor turno"
        self.tablero[coord.f][coord.c] = turno
        self.agrupacionesJugador[turno]
        return

    def agrupacionesDiagonales(self, turno):
        "Devuelte las agrupaciones diagonales que me sirven"
        forms = []
        form = Formacion(Coord(-1, -1), Coord(-1, -1))
        for j in range(19):
            for i in range(19):
                if(j+i == 19):
                    break
                else:
                    if(self.tablero[j+i][j+i] == turno):
                        if form.inicio.f == -1:
                            form.inicio.f = i
                            form.inicio.c = j
                            form.fin.f = i
                            form.fin.c = j
                        else:
                            form.fin.f = i
                            form.fin.c = j
                            if (i == 18):
                                forms.append(form)
                                form = Formacion(Coord(-1, -1), Coord(-1, -1))
                            else:
                                if form.fin.f != -1:
                                    forms.append(form)
                                    form = Formacion(Coord(-1, -1), Coord(-1, -1))
    def agrupacionesV(self, turno):
        "Devuelte las formaciones horizontales que aun me sirven"
        forms = []
        form = Formacion(Coord(-1, -1), Coord(-1, -1))
        for j in range(19):
            for i in range(19):
                if (self.tablero[i][j] == turno):
                    if form.inicio.f == -1:
                        form.inicio.f = i
                        form.inicio.c = j
                        form.fin.f = i
                        form.fin.c = j
                    else:
                        form.fin.f = i
                        form.fin.c = j
                    if (i == 18):
                        forms.append(form)
                        form = Formacion(Coord(-1, -1), Coord(-1, -1))
                else:
                    if form.fin.f != -1:
                        forms.append(form)
                        form = Formacion(Coord(-1, -1), Coord(-1, -1))
        return forms
    def agrupacionesH(self, turno):
        "Devuelte las formaciones horizontales que aun me sirven"
        forms = []
        form = Formacion(Coord(-1, -1), Coord(-1, -1))
        for i in range(19):
            for j in range(19):
                if (self.tablero[i][j] == turno):
                    if form.inicio.f == -1:
                        form.inicio.f = i
                        form.inicio.c = j
                        form.fin.f = i
                        form.fin.c = j
                    else:
                        form.fin.f = i
                        form.fin.c = j
                    if (i == 18):
                        forms.append(form)
                        form = Formacion(Coord(-1, -1), Coord(-1, -1))
                else:
                    if form.fin.f != -1:
                        forms.append(form)
                        form = Formacion(Coord(-1, -1), Coord(-1, -1))
        return forms
    def agrupaciones(self, turno):
        return
    def printagrupacionesH(self, turno):
        "imprime las formaciones horizontales que aun me sirven"
        forms = self.agrupacionesH(turno)
        for e in forms:
            e.printForm()
    def printTablero(self):
        "muestra el tablero actual"
        str1  = " XX | 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18\n"
        str1 += "------------------------------------------------------------------\n"
        for i in range(19):
            for j in range(19):
                if(j == 0):
                    if(i>=10):
                        str1 += " "+ str(i) + " |"
                    else:
                        str1 += " 0"+ str(i) + " |"
                str1 += "  "+str(self.tablero[i][j])
                if(j==18):
                    str1 += "\n"
        print(str1)
def crearTableroVacio():
    "Crea el tablero vacío"
    tablero = []
    for i in range(19):
        linea = []
        for j in range(19):
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




class Formacion:
    def __init__(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin

    def printForm(self):
        print('(' + self.inicio.strCoord() + ',' + self.fin.strCoord() + ')')


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
