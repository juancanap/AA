from Tablero import tablero
from Modelo import modelo
import random
import copy
class juego:
    vectores = []
    def __init__(self):

        self.vectores = []
        self.vectores.append(Coord(0, 1))
        self.vectores.append(Coord(1, 0))
        self.vectores.append(Coord(1, 1))
        self.vectores.append(Coord(-1, 1))
        self.tablero_actual = tablero()
    def copyTablero(self):
        return copy.deepcopy(self.tablero_actual)
    def colocarPieza(self, coord, turno):
        if(coord.f, coord.c) in self.tablero_actual.libres:
            self.tablero_actual.libres.remove((coord.f, coord.c))
        "Coloca en la posicion coord el valor turno"
        self.tablero_actual.tablero[coord.f][coord.c] = turno
        tapado = []
        tapado.append(0)
        tapado.append(0)
        cantidad = []
        cantidad.append(0)
        cantidad.append(0)
        sinficharival= []
        sinficharival.append(0)
        sinficharival.append(0)
        for v in self.vectores:
            j = 0
            tapado[0]= 0
            tapado[1]= 0
            cantidad[0]= 0
            cantidad[1]= 0
            sinficharival[0]= 0
            sinficharival[1]= 0
            modif = []
            for i in range(2):
                estaEnRango = 0 <= coord.f+pow(-1,i)*v.f < 15 and 0 <= coord.c+pow(-1,i)*v.c < 15
                if( estaEnRango and self.tablero_actual.tablero[coord.f+pow(-1,i)*v.f][coord.c+pow(-1,i)*v.c] == turno):
                    l=1
                    estaEnRango = 0 <= coord.f+pow(-1,i)*v.f*l < 15 and 0 <= coord.c+pow(-1,i)*v.c*l < 15
                    while ( estaEnRango and self.tablero_actual.tablero[coord.f+pow(-1,i)*v.f*l][coord.c+pow(-1,i)*v.c*l]== turno):
                        l+= 1
                        estaEnRango = 0 <= coord.f + pow(-1, i) * v.f * l < 15 and 0 <= coord.c + pow(-1,i) * v.c * l < 15
                    cantidad[i] = l - 1
                    if(estaEnRango):
                        if (self.tablero_actual.tablero[coord.f + pow(-1, i) * v.f * l][coord.c + pow(-1, i) * v.c * l] == 0):
                            self.tablero_actual.agrupaciones[turno][l - 1][0] -= 1
                            modif.append(Coord(l-1,0))
                            while (estaEnRango and self.tablero_actual.tablero[coord.f + pow(-1, i) * v.f * l][coord.c + pow(-1, i) * v.c * l] != 3-turno):
                                l += 1
                                estaEnRango = 0 <= coord.f + pow(-1, i) * v.f * l < 15 and 0 <= coord.c + pow(-1,i) * v.c * l < 15
                            tapado[i] = 0
                        else:
                            self.tablero_actual.agrupaciones[turno][l-1][1] -= 1
                            modif.append(Coord(l - 1, 1))
                            tapado[i] = 1

                    else:
                        self.tablero_actual.agrupaciones[turno][l-1][1] -= 1
                        modif.append(Coord(l - 1, 1))
                        tapado[i]=1
                    sinficharival[i] = l - 1

                else:
                    l = 1
                    estaEnRango2 = 0 <= coord.f + pow(-1, i) * v.f * l < 15 and 0 <= coord.c + pow(-1, i) * v.c * l < 15
                    while (estaEnRango2 and self.tablero_actual.tablero[coord.f + pow(-1, i) * v.f * l][coord.c + pow(-1, i) * v.c * l] != 3-turno):
                        l += 1
                        estaEnRango2 = 0 <= coord.f + pow(-1, i) * v.f * l < 15 and 0 <= coord.c + pow(-1,i) * v.c * l < 15
                    sinficharival[i] = l-1
                    if(not(estaEnRango) or (self.tablero_actual.tablero[coord.f+pow(-1,i)*v.f][coord.c+pow(-1,i)*v.c]!= 0)):
                        if(estaEnRango and self.tablero_actual.tablero[coord.f+pow(-1,i)*v.f][coord.c+pow(-1,i)*v.c]== 3-turno):
                            l = 1
                            estaEnRango = 0 <= coord.f + pow(-1, i) * v.f * l < 15 and 0 <= coord.c + pow(-1,i) * v.c * l < 15
                            while (estaEnRango and self.tablero_actual.tablero[coord.f + pow(-1, i) * v.f * l][coord.c + pow(-1, i) * v.c * l] == 3-turno):
                                l += 1
                                estaEnRango = 0 <= coord.f + pow(-1, i) * v.f * l < 15 and 0 <= coord.c + pow(-1,i) * v.c * l < 15
                            if (estaEnRango):
                                if (self.tablero_actual.tablero[coord.f + pow(-1, i) * v.f * l][coord.c + pow(-1, i) * v.c * l] == 0):
                                    self.tablero_actual.agrupaciones[3-turno][l - 1][0] -= 1
                                    cantidadMaxrival = l - 1
                                    estaEnRango = 0 <= coord.f + pow(-1, i) * v.f * l < 15 and 0 <= coord.c + pow(-1,i) * v.c * l < 15
                                    while (estaEnRango and self.tablero_actual.tablero[coord.f + pow(-1, i) * v.f * l][coord.c + pow(-1, i) * v.c * l] != turno and l<=6):
                                        l += 1
                                        estaEnRango = 0 <= coord.f + pow(-1, i) * v.f * l < 15 and 0 <= coord.c + pow(-1, i) * v.c * l < 15
                                    if(l>=6):
                                        self.tablero_actual.agrupaciones[3-turno][cantidadMaxrival][1] += 1

                                else:
                                    self.tablero_actual.agrupaciones[3-turno][l - 1][1] -= 1
                            else:
                                self.tablero_actual.agrupaciones[3-turno][l - 1][1] -= 1

                        tapado[i]=1
            if(sinficharival[0] + sinficharival[1] + 1<5):
                for x in modif:
                    self.tablero_actual.agrupaciones[turno][x.f][x.c] +=1
            else:
                    if (cantidad[0] + 1 + cantidad[1] >= 5):
                        self.tablero_actual.agrupaciones[turno][5][0] += 1
                    else:
                        self.tablero_actual.agrupaciones[turno][cantidad[0] + 1 + cantidad[1]][tapado[0] + tapado[1]] += 1


        return
    def EmularcolocarPieza(self, coord, turno, tableroEmular):
        #print((coord.f,coord.c))
        if(coord.f, coord.c) in tableroEmular.libres:
            tableroEmular.libres.remove((coord.f, coord.c))
        "Coloca en la posicion coord el valor turno"
        tableroEmular.tablero[coord.f][coord.c] = turno;
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
            modif = []
            for i in range(2):
                estaEnRango = 0 <= coord.f+pow(-1,i)*v.f < 15 and 0 <= coord.c+pow(-1,i)*v.c < 15
                if( estaEnRango and tableroEmular.tablero[coord.f+pow(-1,i)*v.f][coord.c+pow(-1,i)*v.c] == turno):
                    l=1
                    estaEnRango = 0 <= coord.f+pow(-1,i)*v.f*l < 15 and 0 <= coord.c+pow(-1,i)*v.c*l < 15
                    while ( estaEnRango and tableroEmular.tablero[coord.f+pow(-1,i)*v.f*l][coord.c+pow(-1,i)*v.c*l]== turno):
                        l+= 1
                        estaEnRango = 0 <= coord.f + pow(-1, i) * v.f * l < 15 and 0 <= coord.c + pow(-1,i) * v.c * l < 15
                    cantidad[i] = l - 1
                    if(estaEnRango):
                        if (tableroEmular.tablero[coord.f + pow(-1, i) * v.f * l][coord.c + pow(-1, i) * v.c * l] == 0):
                            tableroEmular.agrupaciones[turno][l - 1][0] -= 1
                            modif.append(Coord(l-1,0))
                            while (estaEnRango and tableroEmular.tablero[coord.f + pow(-1, i) * v.f * l][coord.c + pow(-1, i) * v.c * l] != 3-turno):
                                l += 1
                                estaEnRango = 0 <= coord.f + pow(-1, i) * v.f * l < 15 and 0 <= coord.c + pow(-1,i) * v.c * l < 15
                            tapado[i] = 0
                        else:
                            tableroEmular.agrupaciones[turno][l-1][1] -= 1
                            modif.append(Coord(l - 1, 1))
                            tapado[i] = 1

                    else:
                        tableroEmular.agrupaciones[turno][l-1][1] -= 1
                        modif.append(Coord(l - 1, 1))
                        tapado[i]=1
                    sinficharival[i] = l - 1

                else:
                    l = 1
                    estaEnRango2 = 0 <= coord.f + pow(-1, i) * v.f * l < 15 and 0 <= coord.c + pow(-1, i) * v.c * l < 15
                    while (estaEnRango2 and tableroEmular.tablero[coord.f + pow(-1, i) * v.f * l][coord.c + pow(-1, i) * v.c * l] != 3-turno):
                        l += 1
                        estaEnRango2 = 0 <= coord.f + pow(-1, i) * v.f * l < 15 and 0 <= coord.c + pow(-1,i) * v.c * l < 15
                    sinficharival[i] = l-1
                    if(not(estaEnRango) or (tableroEmular.tablero[coord.f+pow(-1,i)*v.f][coord.c+pow(-1,i)*v.c]!= 0)):
                        if(estaEnRango and tableroEmular.tablero[coord.f+pow(-1,i)*v.f][coord.c+pow(-1,i)*v.c]== 3-turno):
                            l = 1
                            estaEnRango = 0 <= coord.f + pow(-1, i) * v.f * l < 15 and 0 <= coord.c + pow(-1,i) * v.c * l < 15
                            while (estaEnRango and tableroEmular.tablero[coord.f + pow(-1, i) * v.f * l][coord.c + pow(-1, i) * v.c * l] == 3-turno):
                                l += 1
                                estaEnRango = 0 <= coord.f + pow(-1, i) * v.f * l < 15 and 0 <= coord.c + pow(-1,i) * v.c * l < 15
                            if (estaEnRango):
                                if (tableroEmular.tablero[coord.f + pow(-1, i) * v.f * l][coord.c + pow(-1, i) * v.c * l] == 0):
                                    tableroEmular.agrupaciones[3-turno][l - 1][0] -= 1
                                    cantidadMaxrival = l - 1
                                    estaEnRango = 0 <= coord.f + pow(-1, i) * v.f * l < 15 and 0 <= coord.c + pow(-1,i) * v.c * l < 15
                                    while (estaEnRango and tableroEmular.tablero[coord.f + pow(-1, i) * v.f * l][coord.c + pow(-1, i) * v.c * l] != turno and l<=6):
                                        l += 1
                                        estaEnRango = 0 <= coord.f + pow(-1, i) * v.f * l < 15 and 0 <= coord.c + pow(-1, i) * v.c * l < 15
                                    if(l>=6):
                                        tableroEmular.agrupaciones[3-turno][cantidadMaxrival][1] += 1

                                else:
                                    tableroEmular.agrupaciones[3-turno][l - 1][1] -= 1
                            else:
                                tableroEmular.agrupaciones[3-turno][l - 1][1] -= 1

                        tapado[i]=1
            if(sinficharival[0] + sinficharival[1] + 1 < 5):
                for x in modif:
                    self.tablero_actual.agrupaciones[turno][x.f][x.c] +=1
            else:
                if((cantidad[0]+ 1+ cantidad[1] == 5) or (tapado[0]+ tapado[1] < 2)):
                    if(cantidad[0]+ 1+ cantidad[1] == 5 and tapado[0]+ tapado[1] == 2):
                        tableroEmular.agrupaciones[turno][5][0] +=1
                    else:
                        tableroEmular.agrupaciones[turno][cantidad[0]+ 1+ cantidad[1]][tapado[0]+ tapado[1]] += 1


        return tableroEmular
    def printAgrupaciones(self, turno):
        for i in range(5):
            for j in range(2):
                if i > 0:
                    if j == 0:
                        print(str(i) + " en linea sin bloqueos = "+str(self.tablero_actual.agrupaciones[turno][i][j]))
                    else:
                        print(str(i) + " en linea con bloqueos = " + str(self.tablero_actual.agrupaciones[turno][i][j]))

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
                str1 += "  "+str(self.tablero_actual.tablero[i][j])
                if(j==14):
                    str1 += "\n"
        print(str1)

    def printTablero2(self,tablero):
        "muestra el tablero actual"
        str1 = " XX | 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 \n"
        str1 += "------------------------------------------------------------------\n"
        for i in range(15):
            for j in range(15):
                if (j == 0):
                    if (i >= 10):
                        str1 += " " + str(i) + " |"
                    else:
                        str1 += " 0" + str(i) + " |"
                str1 += "  " + str(tablero.tablero[i][j])
                if (j == 14):
                    str1 += "\n"
        print(str1)

    def determinarMejorMovimiento(self,turno,tablero_em):
        max_valor = -100
        movidasMejores = []
        max_coord = (-1, -1)
        for (x, y) in self.tablero_actual.libres:
           tablero_prueba = copy.deepcopy(tablero_em)
           tablero = juego.EmularcolocarPieza(Coord(x,y),turno,tablero_prueba)
           valor = modelo.funcionbjetivo(tablero,turno)
           if valor > max_valor:
               movidasMejores = []
               max_valor = valor
               max_coord = (x, y)
               movidasMejores.append(max_coord)
           if valor == max_valor:
               max_coord = (x, y)
               movidasMejores.append(max_coord)
        posicion = int(random.uniform(0, len(movidasMejores)))
        max_coord =  movidasMejores[posicion]
        return [max_valor, max_coord]

    def jugar_vs_aleatorio(self, turno):
        for (x, y) in juego.tablero_actual.libres:
            if turno == 1:
                [valor, (a, b)] = juego.determinarMejorMovimiento(turno, juego.tablero_actual)
                juego.colocarPieza(Coord(a, b), turno)
                juego.printTablero()
            else:
                # [valor, (a, b)] = juego.determinarMejorMovimiento(turno, juego.tablero_actual)
                posicion = int(random.uniform(0,len(juego.tablero_actual.libres)))
                (a,b) =  juego.tablero_actual.libres[posicion]
                juego.colocarPieza(Coord(a, b), turno)
                juego.printTablero()
            if juego.tablero_actual.JuegoFinalizado():
                print("Ganador jugador: " + str(turno))
                break
            else:
                if turno == 1:
                    turno = 2
                else:
                    turno = 1

    def jugar_vs_si_mismo(self, turno):
        for (x, y) in juego.tablero_actual.libres:
            if turno == 1:
                [valor, (a, b)] = juego.determinarMejorMovimiento(turno, juego.tablero_actual)
                juego.colocarPieza(Coord(a, b), turno)
                juego.printTablero()
            else:
                [valor, (a, b)] = juego.determinarMejorMovimiento(turno, juego.tablero_actual)
                # posicion = int(random.uniform(0, len(juego.tablero_actual.libres)))
                # (a, b) = juego.tablero_actual.libres[posicion]
                juego.colocarPieza(Coord(a, b), turno)
                juego.printTablero()
            if juego.tablero_actual.JuegoFinalizado():
                print("Ganador jugador: " + str(turno))
                break
            else:
                if turno == 1:
                    turno = 2
                else:
                    turno = 1

    def jugar_vs_humano(self, turno):
        for (x, y) in juego.tablero_actual.libres:
            if turno == 1:
                [valor, (a, b)] = juego.determinarMejorMovimiento(turno, juego.tablero_actual)
                juego.colocarPieza(Coord(a, b), turno)
                juego.printTablero()
            else:
                a = input("ingrese fila:")
                b = input("ingrese columna:")
                # [valor, (a, b)] = juego.determinarMejorMovimiento(turno, juego.tablero_actual)
                # posicion = int(random.uniform(0, len(juego.tablero_actual.libres)))
                # (a, b) = juego.tablero_actual.libres[posicion]
                juego.colocarPieza(Coord(int(a), int(b)), turno)
                juego.printTablero()
            if juego.tablero_actual.JuegoFinalizado():
                print("Ganador jugador: " + str(turno))
                break
            else:
                if turno == 1:
                    turno = 2
                else:
                    turno = 1

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
        self.rival = rival


modelo = modelo()
juego = juego()
"""
print(len(juego.tablero_actual.libres))
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
juego.colocarPieza(Coord(2, 4), 1)
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
juego.colocarPieza(Coord(0, 0), 2)
juego.colocarPieza(Coord(10, 10), 2)
juego.colocarPieza(Coord(14, 14), 1)
print("Mis agrupaciones:")
juego.printAgrupaciones(1)
print("Sus agrupaciones:")
juego.printAgrupaciones(2)
juego.printTablero()
mejor_mov = juego.determinarMejorMovimiento(1,juego.tablero_actual)
print(mejor_mov)
"""
turno = 1
"""
for (x,y) in juego.tablero_actual.libres:

    [valor,(a,b)]= juego.determinarMejorMovimiento(turno, juego.tablero_actual)
    juego.colocarPieza(Coord(a, b), turno)
    if juego.tablero_actual.JuegoFinalizado():
        juego.printTablero()
        print("Ganador jugador: "+ str(turno))

        break
    else:
        if turno == 1:
            turno = 2
        else:
            turno = 1
    juego.printTablero()
"""
juego.jugar_vs_humano(turno)

# for (x,y) in juego.tablero_actual.libres:
#     if turno == 1:
#         [valor,(a,b)]= juego.determinarMejorMovimiento(turno, juego.tablero_actual)
#         juego.colocarPieza(Coord(a, b), turno)
#         juego.printTablero()
#     else:
#         [valor, (a, b)] = juego.determinarMejorMovimiento(turno, juego.tablero_actual)
#         #posicion = int(random.uniform(0,len(juego.tablero_actual.libres)))
#         #(a,b) =  juego.tablero_actual.libres[posicion]
#         juego.colocarPieza(Coord(a, b), turno)
#         juego.printTablero()
#     if juego.tablero_actual.JuegoFinalizado():
#         print("Ganador jugador: "+ str(turno))
#
#         break
#     else:
#         if turno == 1:
#             turno = 2
#         else:
#             turno = 1


i = 1