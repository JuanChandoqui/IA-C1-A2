from matplotlib import markers
import matplotlib.pyplot as plt

class Grafica:
    def __init__(self, mejores, peores, promedio):
        self.mejores = mejores
        self.peores = peores
        self.promedio = promedio
        # self.generarGrafica()
        # self.generarGraficaMarcadores()

    def generarGrafica(self):
        plt.plot(self.mejores, label="Mejor caso")
        plt.plot(self.promedio,label="Caso promedio")
        plt.plot(self.peores, label="Peor Caso")
        plt.legend()
        plt.xlabel("Iteraciones")
        plt.ylabel("Aptitud")
        plt.title("EvolucionGeneraciones")
        plt.show()

    def generarGraficaPuntos(x, y, generacion):
        plt.scatter(x, y, label="Individuo")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title(f"Numero de generación: {generacion}")
        fig=plt.figure()
        # plt.ion()
        # plt.ioff() 
        plt.close(fig)     
        plt.savefig(f'./Resources/Images/{generacion}.png')
        plt.clf()


    def generarGraficaMarcadores(self):
        plt.plot(self.mejores, label="Mejor caso", marker = 'o')
        plt.plot(self.promedio,label="Caso promedio",  marker = 'o')
        plt.plot(self.peores, label="Peor Caso",  marker = 'o')
        plt.legend()
        plt.xlabel("Iteraciones")
        plt.ylabel("Aptitud")
        plt.title("EvolucionGeneraciones")
        plt.show()
