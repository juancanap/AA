class Juego:
    vectores =[]
    def __init__(self):

        self.vectores = []
        self.vectores.append(Coord(0,1))
        self.vectores.append(Coord(1,0))
        self.vectores.append(Coord(1,1))
        self.vectores.append(Coord(-1,1))
        self.agrupaciones = []
        self.agrupaciones.append([])
        self.agrupaciones.append([])
        self.agrupaciones.append([])
        for i in range(5):
            lista1 = []
            for j in range(2):
                lista1.append(0)
            self.agrupaciones[1].append(lista1)
            self.agrupaciones[2].append(lista1.copy())
        self.tablero = crearTableroVacio()

    def colocarPieza(self, coord, turno):
        "Coloca en la posicion coord el valor turno"
        self.tablero[coord.f][coord.c] = turno;
        tapado =[]
        tapado.append(0)
        tapado.append(0)
        cantidad = []
        cantidad.append(0)
        cantidad.append(0)
        sinficharival = []
        sinficharival.append(0)
        sinficharival.append(0)
        for v in self.vectores:
            j=0
            tapado[0]= 0
            tapado[1]= 0
            cantidad[0]= 0
            cantidad[1]= 0
            sinficharival[0]= 0
            sinficharival[1]= 0
            for i in range(2):
                estaEnRango = 0 <= coord.f+pow(-1,i)*v.f < 15 and 0 <= coord.c+pow(-1,i)*v.c < 15
                if( estaEnRango and self.tablero[coord.f+pow(-1,i)*v.f][coord.c+pow(-1,i)*v.c] == turno):
                    l=1
                    estaEnRango = 0 <= coord.f+pow(-1,i)*v.f*l < 15 and 0 <= coord.c+pow(-1,i)*v.c*l < 15
                    while ( estaEnRango and self.tablero[coord.f+pow(-1,i)*v.f*l][coord.c+pow(-1,i)*v.c*l]== turno):
                        l+= 1
                        estaEnRango = 0 <= coord.f + pow(-1, i) * v.f * l < 15 and 0 <= coord.c + pow(-1,i) * v.c * l < 15
                    cantidad[i] = l - 1
                    if(estaEnRango):
                        if (self.tablero[coord.f + pow(-1, i) * v.f * l][coord.c + pow(-1, i) * v.c * l] == 0):
                            self.agrupaciones[turno][l - 1][0] -= 1
                            while (estaEnRango and self.tablero[coord.f + pow(-1, i) * v.f * l][coord.c + pow(-1, i) * v.c * l] != 3-turno):
                                l += 1
                                estaEnRango = 0 <= coord.f + pow(-1, i) * v.f * l < 15 and 0 <= coord.c + pow(-1,i) * v.c * l < 15
                            tapado[i] = 0
                        else:
                            self.agrupaciones[turno][l-1][1] -= 1
                            tapado[i] = 1

                    else:
                        self.agrupaciones[turno][l-1][1] -= 1
                        tapado[i]=1
                    sinficharival[i] = l - 1

                else:
                    l = 1
                    estaEnRango2 = 0 <= coord.f + pow(-1, i) * v.f * l < 15 and 0 <= coord.c + pow(-1, i) * v.c * l < 15
                    while (estaEnRango2 and self.tablero[coord.f + pow(-1, i) * v.f * l][coord.c + pow(-1, i) * v.c * l] != 3-turno):
                        l += 1
                        estaEnRango2 = 0 <= coord.f + pow(-1, i) * v.f * l < 15 and 0 <= coord.c + pow(-1,i) * v.c * l < 15
                    sinficharival[i] = l-1
                    if(not(estaEnRango) or (self.tablero[coord.f+pow(-1,i)*v.f][coord.c+pow(-1,i)*v.c]!= 0)):
                        if(self.tablero[coord.f+pow(-1,i)*v.f][coord.c+pow(-1,i)*v.c]== 3-turno):
                            l = 1
                            estaEnRango = 0 <= coord.f + pow(-1, i) * v.f * l < 15 and 0 <= coord.c + pow(-1,i) * v.c * l < 15
                            while (estaEnRango and self.tablero[coord.f + pow(-1, i) * v.f * l][coord.c + pow(-1, i) * v.c * l] == 3-turno):
                                l += 1
                                estaEnRango = 0 <= coord.f + pow(-1, i) * v.f * l < 15 and 0 <= coord.c + pow(-1,i) * v.c * l < 15
                            if (estaEnRango):
                                if (self.tablero[coord.f + pow(-1, i) * v.f * l][coord.c + pow(-1, i) * v.c * l] == 0):
                                    self.agrupaciones[3-turno][l - 1][0] -= 1
                                    cantidadMaxrival = l - 1
                                    estaEnRango = 0 <= coord.f + pow(-1, i) * v.f * l < 15 and 0 <= coord.c + pow(-1,i) * v.c * l < 15
                                    while (estaEnRango and self.tablero[coord.f + pow(-1, i) * v.f * l][coord.c + pow(-1, i) * v.c * l] != turno):
                                        l += 1
                                        estaEnRango = 0 <= coord.f + pow(-1, i) * v.f * l < 15 and 0 <= coord.c + pow(-1, i) * v.c * l < 15
                                    if(l>=6):
                                        self.agrupaciones[3-turno][cantidadMaxrival][1] += 1

                                else:
                                    self.agrupaciones[3-turno][l - 1][1] -= 1
                            else:
                                self.agrupaciones[3-turno][l - 1][1] -= 1

                        tapado[i]=1
            if(tapado[0]+ tapado[1] < 2 and sinficharival[0] + sinficharival[1] + 1 >= 5):
                self.agrupaciones[turno][cantidad[0]+ 1+ cantidad[1]][tapado[0]+ tapado[1]] += 1


        return
    def printAgrupaciones(self, turno):
        for i in range(5):
            for j in range(2):
                if i>0:
                    if(j == 0):
                        print(str(i)+ " en linea sin bloqueos = "+str(self.agrupaciones[turno][i][j]))
                    else:
                        print(str(i) + " en linea con bloqueos = " + str(self.agrupaciones[turno][i][j]))

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
        self.coord = coord;
        self.rival =  rival;

juego = Juego()
juego.colocarPieza(Coord(0, 1), 1)
print("Mis agrupaciones:")
juego.printAgrupaciones(1)
print("Sus agrupaciones:")
juego.printAgrupaciones(2)
juego.printTablero()
juego.colocarPieza(Coord(0, 2), 2)
print("Mis agrupaciones:")
juego.printAgrupaciones(1)
print("Sus agrupaciones:")
juego.printAgrupaciones(2)
juego.printTablero()
juego.colocarPieza(Coord(0, 3), 1)
print("Mis agrupaciones:")
juego.printAgrupaciones(1)
print("Sus agrupaciones:")
juego.printAgrupaciones(2)
juego.printTablero()
juego.colocarPieza(Coord(1, 1), 2)
print("Mis agrupaciones:")
juego.printAgrupaciones(1)
print("Sus agrupaciones:")
juego.printAgrupaciones(2)
juego.printTablero()
juego.colocarPieza(Coord(2, 1), 1)
print("Mis agrupaciones:")
juego.printAgrupaciones(1)
print("Sus agrupaciones:")
juego.printAgrupaciones(2)
juego.printTablero()
juego.colocarPieza(Coord(3, 1), 2)
print("Mis agrupaciones:")
juego.printAgrupaciones(1)
print("Sus agrupaciones:")
juego.printAgrupaciones(2)
juego.printTablero()
juego.colocarPieza(Coord(2, 2), 1)
print("Mis agrupaciones:")
juego.printAgrupaciones(1)
print("Sus agrupaciones:")
juego.printAgrupaciones(2)
juego.printTablero()
juego.colocarPieza(Coord(4, 1), 2)
print("Mis agrupaciones:")
juego.printAgrupaciones(1)
print("Sus agrupaciones:")
juego.printAgrupaciones(2)
juego.printTablero()
juego.colocarPieza(Coord(2, 3), 1)
print("Mis agrupaciones:")
juego.printAgrupaciones(1)
print("Sus agrupaciones:")
juego.printAgrupaciones(2)
juego.printTablero()
juego.colocarPieza(Coord(5, 1), 2)
print("Mis agrupaciones:")
juego.printAgrupaciones(1)
print("Sus agrupaciones:")
juego.printAgrupaciones(2)
juego.printTablero()
juego.colocarPieza(Coord(2, 4), 1)
print("Mis agrupaciones:")
juego.printAgrupaciones(1)
print("Sus agrupaciones:")
juego.printAgrupaciones(2)
juego.printTablero()

i = 1
