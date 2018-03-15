# -*- coding: utf-8 -*-
from random import randint

set_instancias = [
    ('A', 'A', 'N', 'M', 'B', u'Sí'),
    ('B', 'M', 'M', 'A', 'M', u'No'),
    ('M', 'A', 'N', 'M', 'M', u'Sí'),
    ('M', 'A', 'M', 'A', 'B', u'No'),
]

posibles = [
    ['A', 'M', 'B'],
    ['A', 'M', 'B'],
    ['M', 'N'],
    ['A', 'M', 'B'],
    ['B', 'M'],
]


def findS(set_instancias):
    concepto = ['Ninguno', 'Ninguno', 'Ninguno', 'Ninguno', 'Ninguno']

    for inst in set_instancias:
        if inst[5] == u'Sí':
            for index in range(5):
                if 'Ninguno' in concepto[index]:
                    concepto[index] = inst[index]
                elif not inst[index] in concepto[index]:
                    concepto[index] = '?'
    return concepto


def findSRandom(concepto_objetivo):
    total = 0
    positivos = 0
    concepto = ['Ninguno', 'Ninguno', 'Ninguno', 'Ninguno', 'Ninguno']

    while concepto != concepto_objetivo:
        total += 1
        instancia = ['', '', '', '', '', '']
        instancia[0] = posibles[0][randint(0, 2)]
        instancia[1] = posibles[1][randint(0, 2)]
        instancia[2] = posibles[2][randint(0, 1)]
        instancia[3] = posibles[3][randint(0, 2)]
        instancia[4] = posibles[4][randint(0, 1)]
        if instancia[1] == 'M':
            positivos += 1
            instancia[5] = u'Sí'
            print("Instancia generada: ", instancia)
            for index in range(5):
                if 'Ninguno' in concepto[index]:
                    concepto[index] = instancia[index]
                elif not instancia[index] in concepto[index]:
                    concepto[index] = '?'
        else:
            instancia[5] = u'No'
            print("Instancia generada: ", instancia)
    return concepto, total, positivos


def execute(cant_exec):
    totales = []
    positivos = []
    objetivo = ['?', 'M', '?', '?', '?']
    for ex in range(cant_exec):
        concepto_resultado, total, pos = findSRandom(objetivo)
        totales.append(total)
        positivos.append(pos)
        print("Resultado ", ex, ": ", concepto_resultado)

    promedio_total = 0
    promedio_pos = 0
    for i in range(cant_exec):
        promedio_total += totales[i]
        promedio_pos += positivos[i]
    print("\n\n")
    print("RESULTADOS FINALES -----")
    print("Promedio total de instancias necesarias: ", promedio_total/cant_exec)
    print("Promedio total de instancias POSITIVAS necesarias: ", promedio_pos/cant_exec)


print("\n\n")
print("------------ ejercicios a y b -----------")
resultado = findS(set_instancias)
print("Resultado: ", resultado)

print("\n\n")
print("------------ ejercicio c -----------")
cant_exec = 1000
execute(cant_exec)
