from Tablero import tablero
from gomoku import Juego
class modelo:
    def __init__(self):
        self.pesos = [0.000025, 0.000010, 0.00045, 0.00020, 0.006, 0.003, 0.9, 0.40, -0.000025, -0.000010, -0.00045, -0.00020, -0.006, -0.003, -30, -30, 100,-100]
        self.coeficiente_aprendizaje = 0
        self.ValorEntrenamiento = 0

    def funcionbjetivo(self, tablero,turno):

        uno_en_linea_sin_bloq = tablero.agrupaciones[turno][1][0]
        uno_en_linea_con_bloq = tablero.agrupaciones[turno][1][1]
        dos_en_linea_sin_bloq = tablero.agrupaciones[turno][2][0]
        dos_en_linea_con_bloq = tablero.agrupaciones[turno][2][1]
        tres_en_linea_sin_bloq = tablero.agrupaciones[turno][3][0]
        tres_en_linea_con_bloq = tablero.agrupaciones[turno][3][1]
        cuatro_en_linea_sin_bloq = tablero.agrupaciones[turno][4][0]
        cuatro_en_linea_con_bloq = tablero.agrupaciones[turno][4][1]
        cinco_en_linea = tablero.agrupaciones[turno][5][0] + tablero.agrupaciones[turno][5][1]

        uno_en_linea_sin_bloq_rival = tablero.agrupaciones[3-turno][1][0]
        uno_en_linea_con_bloq_rival = tablero.agrupaciones[3-turno][1][1]
        dos_en_linea_sin_bloq_rival = tablero.agrupaciones[3-turno][2][0]
        dos_en_linea_con_bloq_rival = tablero.agrupaciones[3-turno][2][1]
        tres_en_linea_sin_bloq_rival = tablero.agrupaciones[3-turno][3][0]
        tres_en_linea_con_bloq_rival = tablero.agrupaciones[3-turno][3][1]
        cuatro_en_linea_sin_bloq_rival = tablero.agrupaciones[3-turno][4][0]
        cuatro_en_linea_con_bloq_rival = tablero.agrupaciones[3-turno][4][1]
        cinco_en_linea_rival = tablero.agrupaciones[3-turno][5][0] + tablero.agrupaciones[3-turno][5][1]

        valor = self.pesos[0] * uno_en_linea_sin_bloq + self.pesos[1] * uno_en_linea_con_bloq + self.pesos[2] * dos_en_linea_sin_bloq + \
                self.pesos[3] * dos_en_linea_con_bloq + self.pesos[4] * tres_en_linea_sin_bloq + \
                self.pesos[5] * tres_en_linea_con_bloq + self.pesos[6] * cuatro_en_linea_sin_bloq + \
                self.pesos[7] * cuatro_en_linea_con_bloq + self.pesos[8] * uno_en_linea_sin_bloq_rival + \
                self.pesos[9] * uno_en_linea_con_bloq_rival + self.pesos[10] * dos_en_linea_sin_bloq_rival + \
                self.pesos[11] * dos_en_linea_con_bloq_rival + self.pesos[12] * tres_en_linea_sin_bloq_rival + \
                self.pesos[13] * tres_en_linea_con_bloq_rival + self.pesos[14] * cuatro_en_linea_sin_bloq_rival +\
                self.pesos[15] * cuatro_en_linea_con_bloq_rival + self.pesos[16] * cinco_en_linea +\
                self.pesos[17] * cinco_en_linea_rival

        return valor

    def actualizarpesos(self, t_ent, t_op):
        for i in range(0, len(self.pesos)-1):
            self.pesos[i] = self.pesos[i] + self.coeficiente_aprendizaje * (self.funcionbjetivo(t_ent) - self.funcionbjetivo(t_op))
        return


