import matplotlib.pyplot as plt

class Grafica:
    def __init__(self, mejores, peores, promedio):
        self.mejores = mejores
        self.peores = peores
        self.promedio = promedio
        self.generarGrafica()

    def generarGrafica(self):
        plt.plot(self.mejores, label="Mejor caso",)
        plt.plot(self.promedio,label="Caso promedio")
        plt.plot(self.peores,label="Peor Caso")
        plt.legend()
        plt.xlabel("Iteraciones")
        plt.ylabel("Aptitud")
        plt.title("EvolucionGeneraciones")
        plt.show()