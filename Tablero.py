
class tablero:
    def __init__(self):
        self.agrupaciones = []                       #              |     JUGADOR 1    |     JUGADOR 2     |
        self.agrupaciones.append([])                 #                s/bloq | c/bloq  |  s/bloq | c/bloq  |
        self.agrupaciones.append([])                 # 1 EN LINEA   |        |         |         |         |
        self.agrupaciones.append([])                 # 2 EN LINEA   |        |         |         |         |
                                                     # 3 EN LINEA   |        |         |         |         |
                                                     # 4 EN LINEA   |        |         |         |         |
                                                     # 5 EN LINEA   |                  |                   |

        for i in range(10):
            listaAux = []
            for j in range(2):
                listaAux.append(0)
            self.agrupaciones[1].append(listaAux)
            self.agrupaciones[2].append(listaAux.copy())

        self.tablero = self.crearTableroVacio()
        self.libres = [(c, p) for c in range(0, 15) for p in range(0, 15)]

    def crearTableroVacio(self):
        "Crea el tablero vacío"
        tablero = []
        for i in range(15):
            linea = []
            for j in range(15):
                linea.append(0)
            tablero.append(linea)
        return tablero
    def JuegoFinalizado(self):
        if self.agrupaciones[1][5][0] == 1 or self.agrupaciones[2][5][0] == 1 or self.agrupaciones[1][5][1] == 1 or self.agrupaciones[2][5][1] == 1:
            return True
        return False
