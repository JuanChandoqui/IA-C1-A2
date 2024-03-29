from asyncio.windows_events import NULL
from math import log, sqrt
import math
import random
from statistics import mean
from pandas import DataFrame

from Models.grafica import Grafica
from Models.video import generarVideo


class Poblacion:
    def __init__(self, tamPobIni, TamPobMax, resolucion_x, resolucion_y, x_min, x_max, y_min, y_max, pmi, pmg, niteraciones,opcion, opcion_grafica):
        self.tamPobIni = tamPobIni
        self.tamPobMax = TamPobMax
        self.resolucion_x = resolucion_x
        self.resolucion_y = resolucion_y
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.pmi = pmi
        self.pmg = pmg
        self.niteraciones=niteraciones
        self.opcion=opcion
        self.opcion_grafica=opcion_grafica
        self.mejores = []
        self.peores = []
        self.promedio = []
        self.calcular_datos()
        self.inicializar()
        self.generaciones()

    def calcular_datos(self):
        self.calculate_rx()
        self.calculate_ry()
        self.calculate_npx()
        self.calculate_npy()
        self.calculate_rango_i()
        self.calculate_rango_j()
        self.calculate_nbx()
        self.calculate_nby()

    def calculate_rx(self):
        self.rx = self.x_max - self.x_min

    def calculate_ry(self):
        self.ry = self.y_max - self.y_min

    def calculate_npx(self):
        self.npx = int(round((self.rx/self.resolucion_x) + 1, 0))

    def calculate_npy(self):
        self.npy = int(round((self.ry/self.resolucion_y) + 1, 0))

    def calculate_rango_i(self):
        self.rango_i = (0, self.npx-1)

    def calculate_rango_j(self):
        self.rango_j = (0, self.npy-1)

    def calculate_nbx(self):
        self.nbx = len(bin(self.npx)[2:])

    def calculate_nby(self):
        self.nby = len(bin(self.npy)[2:])

    def inicializar(self):
        self.individuos = []
        while len(self.individuos) < self.tamPobIni:
            for _ in range(self.tamPobIni-len(self.individuos)):
                genotipo = [str(random.randint(0, 1))
                            for _ in range(self.nbx+self.nby)]
                self.individuos.append(Individuo(
                    genotipo, self.nbx, self.nby, self.x_min, self.y_min, self.resolucion_x, self.resolucion_y))
            self.evaluar_individuos()
        puntos_x = [ i.x for i in self.individuos]
        puntos_y = [ i.y for i in self.individuos]
        Grafica.generarGraficaPuntos(puntos_x, puntos_y, 0,self.mejorSolucion())
        self.procesos()
        
    
    def procesos(self):
        self.cruza()
        self.mutacion()
        self.evaluar_individuos()
        self.MejorCaso()
        self.PeorCaso()
        self.Promedio()
        self.PODA()

    
    def generaciones(self):
        for generacion in range(1,self.niteraciones):
            self.procesos()
            puntos_x = [ i.x for i in self.individuos]
            puntos_y = [ i.y for i in self.individuos]
            Grafica.generarGraficaPuntos(puntos_x, puntos_y, generacion,self.mejorSolucion())
        Grafica(self.mejores, self.peores, self.promedio)
        if(self.opcion_grafica == 1):
            Grafica.generarGrafica(self)
        elif (self.opcion_grafica == 2):
            Grafica.generarGraficaMarcadores(self)
        generarVideo()
        
    
    def evaluar_individuos(self):
        temp_individuos = []
        for individuo in self.individuos:
            if individuo.i >= self.rango_i[0] and individuo.i <= self.rango_i[1] and individuo.j >= self.rango_j[0] and individuo.j <= self.rango_j[1] and individuo.calculate_aptitud()!=0:
                temp_individuos.append(individuo)
        self.individuos = temp_individuos

    def cruza(self):
        temp_individuos = self.individuos
        padres = []
        self.hijos = []

        indices = random.sample(
            range(len(temp_individuos)), len(temp_individuos))
        padres = [indices[i:i + 2] for i in range(0, len(indices), 2)]

        for indice_individuo in padres:
            if len(indice_individuo) == 2:
                padre = self.individuos[indice_individuo[0]].genotipo
                madre = self.individuos[indice_individuo[1]].genotipo
                puntos_cruza = sorted(random.sample(
                    range(1, (self.nbx+self.nby)-1), 3))
                hijo1 = []
                hijo2 = []
                for indice in range(self.nbx+self.nby):
                    if indice < puntos_cruza[0]:
                        hijo1.append(padre[indice])
                        hijo2.append(madre[indice])
                    elif indice > puntos_cruza[0] and indice < puntos_cruza[1]:
                        hijo1.append(madre[indice])
                        hijo2.append(padre[indice])
                    elif indice > puntos_cruza[1] and indice < puntos_cruza[2]:
                        hijo1.append(padre[indice])
                        hijo2.append(madre[indice])
                    else:
                        hijo1.append(madre[indice])
                        hijo2.append(padre[indice])
                self.hijos.append(hijo1)
                self.hijos.append(hijo2)
            else:
                self.individuos.pop(indice_individuo[0])

    def mutacion(self):
        for index_individuo in range(len(self.hijos)):
            individuo = self.hijos[index_individuo]
            pmi_actual = random.uniform(0, 1)
            if pmi_actual <= self.pmi:
                for index_gen in range(len(individuo)):
                    pmg_actual = random.uniform(0, 1)
                    if pmg_actual <= self.pmg:
                        if individuo[index_gen] == '0':
                            individuo[index_gen] = '1'
                        elif individuo[index_gen] == '1':
                            individuo[index_gen] = '0'
        self.individuos = self.individuos + \
            [Individuo(i, self.nbx, self.nby, self.x_min, self.y_min,
                       self.resolucion_x, self.resolucion_y) for i in self.hijos]

    def MejorCaso(self):
        aptitudes = [i.calculate_aptitud() for i in self.individuos]
        if self.opcion == 0:
            self.mejores.append(max(aptitudes))
        else:
            self.mejores.append(min(aptitudes))

    def PeorCaso(self):
        aptitudes = [i.calculate_aptitud() for i in self.individuos]
        if self.opcion == 0:
            self.peores.append(min(aptitudes))
        else:
            self.peores.append(max(aptitudes))
    
    def Promedio(self):
        aptitudes = [i.calculate_aptitud() for i in self.individuos]
        self.promedio.append(mean(aptitudes))
    
    def PODA(self):
        temp_individuos = []
        for index in range(len(self.individuos)): # Elimina elementos que no tiene solucion fitness
            if self.individuos[index].calculate_aptitud() != 0:
                temp_individuos.append(self.individuos[index])
        self.individuos = temp_individuos

        aptitudes = [i.calculate_aptitud() for i in self.individuos]
        data = {'individuo': self.individuos, 'aptitud':aptitudes}
        df = DataFrame(data)

        if len(self.individuos) > self.tamPobMax: # Cuando excede el tamaño de la poblacion
            df = df.drop_duplicates(['aptitud']) # Elimina elementos repetidos (clones)
            # self.individuos = temp_individuos
            if len(self.individuos) > self.tamPobMax:
                if self.opcion == 0:
                    df = df.sort_values(by='aptitud',ascending=False)
                else:
                    df = df.sort_values(by='aptitud',ascending=True)
                temp_individuos = list(df['individuo'][0:self.tamPobMax])
                self.individuos = temp_individuos

    def mejorSolucion(self):
        aptitudes = [i.calculate_aptitud() for i in self.individuos]
        data = {'individuo': self.individuos, 'aptitud':aptitudes}
        df = DataFrame(data)
        if self.opcion == 0:
            df = df.sort_values(by='aptitud',ascending=False)
        else:
            df = df.sort_values(by='aptitud',ascending=True)
        return {'cromosoma':df['individuo'][0].getGenotipo(),
                'cromosomaN':df['individuo'][0].getGenotipoNumero(),
                'fenotipo': (df['individuo'][0].x,df['individuo'][0].y),
                'fitness': df['individuo'][0].calculate_aptitud()}
class Individuo:
    def __init__(self, genotipo, nbx, nby, x_min, y_min, rx, ry):
        self.genotipo = genotipo
        self.set_i_j(nbx, nby)
        self.set_x_y(x_min, y_min, rx, ry)

    def getGenotipo(self):
        return ''.join(self.bits_i + self.bits_j)
    
    def getGenotipoNumero(self):
        return int(''.join(self.bits_i + self.bits_j),2)

    def set_i_j(self, nbx, nby):
        self.bits_i = self.genotipo[0:nbx]
        self.bits_j = self.genotipo[nbx:(nbx+nby)]
        self.i = int(''.join(self.bits_i), 2)
        self.j = int(''.join(self.bits_j), 2)

    def set_x_y(self, a, c, rx, ry):
        self.x = round(a + (self.i * rx), 2)
        self.y = round(c + (self.j * ry), 2)

    def calculate_aptitud(self):  # fitness
        fitness = 0
        try:
            fitness = sqrt(self.x) - (3*log(((self.x**2)+(self.y**2))*(-self.x+(2*self.y)-(1/3))))
        except ValueError:
            pass
        return fitness
        

# if __name__ == '__main__':
#     Poblacion(10, 15, 0.7, 0.7, 3, 10, 50, 85, 0.481, 0.002,10,0)