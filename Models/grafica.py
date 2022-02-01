import matplotlib.pyplot as plt

class Grafica:
    def __init__(self, mejores, peores, promedio):
        self.mejores = mejores
        self.peores = peores
        self.promedio = promedio

    def generarGrafica(self):
        plt.plot(self.mejores, label="Mejor caso")
        plt.plot(self.promedio,label="Caso promedio")
        plt.plot(self.peores, label="Peor Caso")
        plt.legend()
        plt.xlabel("Iteraciones")
        plt.ylabel("Aptitud")
        plt.title("EvolucionGeneraciones")
        plt.show()

    def generarGraficaPuntos(x, y, generacion,mejorIndividuo):
        plt.scatter(x, y)
        plt.scatter(mejorIndividuo['fenotipo'][0], mejorIndividuo['fenotipo'][1], label="Mejor individuo")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title(f"Numero de generación: {generacion}")
        plt.legend()
        fig=plt.figure()
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
