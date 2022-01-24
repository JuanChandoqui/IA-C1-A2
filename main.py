import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
from PyQt5 import uic
from numpy import double
from Models.AG import Poblacion 

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./Views/main.ui', self)
        self.pushButton_iniciarAlgoritmo.clicked.connect(self.iniciarAlgoritmo)
        self.radioButton_GraficaLineas.toggled.connect( lambda checked: checked and self.radioButton_GraficaMarcadores.setChecked(False))
        self.radioButton_GraficaMarcadores.toggled.connect( lambda checked: checked and self.radioButton_GraficaLineas.setChecked(False))
        self.radioButton_Maximizar.setChecked(True)

    def iniciarAlgoritmo(self):     
        tamPobIni = int(self.spinBox_tamPobIni.value())
        tamPobMax = int(self.spinBox_tamPobMax.value())
        resolucionX = double(self.doubleSpinBox__resolucionX.value())
        resolucionY = double(self.doubleSpinBox_resolucionY.value())
        rangoXmin = double(self.doubleSpinBox_Xmin.value())
        rangoYmin = double(self.doubleSpinBox_Ymin.value())
        rangoXmax = double(self.doubleSpinBox_Xmax.value())
        rangoYmax = double(self.doubleSpinBox_Ymax.value())
        probMutacionInd = double(self.doubleSpinBox__probMutacionInd.value())
        probMutacionGen = double(self.doubleSpinBox__probMutacionGen.value())
        numIteraciones = int(self.spinBox_numIteraciones.value())
        opcion = 0 #0 --> MAXIMIZAR & 1 --> MINIMIZAR
        opcion_grafica = 1
        
        if (self.radioButton_GraficaLineas.isChecked()):      
            opcion_grafica = 1
        elif (self.radioButton_GraficaMarcadores.isChecked()):
            opcion_grafica = 2

        if (tamPobIni > 0):
            if(tamPobIni <= tamPobMax):
                if(numIteraciones > 0):
                    if(rangoXmin < rangoYmax or rangoYmin  < rangoYmax):
                        if((rangoXmin > 0 and rangoYmin > 0) or (rangoXmax > 0 and rangoYmax > 0)):
                            if self.radioButton_Maximizar.isChecked():
                                opcion = 0
                                Poblacion(tamPobIni, tamPobMax, resolucionX, resolucionY, rangoXmin, rangoXmax, rangoYmin, rangoYmax, probMutacionInd, probMutacionGen, numIteraciones, opcion, opcion_grafica)
                            elif self.radioButton_Minimizar.isChecked():      
                                opcion = 1
                                Poblacion(tamPobIni, tamPobMax, resolucionX, resolucionY, rangoXmin, rangoXmax, rangoYmin, rangoYmax, probMutacionInd, probMutacionGen, numIteraciones, opcion, opcion_grafica)
                        else:
                            self.dialogoDeMensaje("No existe espacio de solución")
                    else: 
                        self.dialogoDeMensaje("Introduce valores validos, no son aceptables para la generación del rango")
                else:
                    self.dialogoDeMensaje("El numero de iteracciones es invalida, introduce una cantidad valida")
            else:
                self.dialogoDeMensaje("El numero del tamaño de la población inicial no puede ser mayor al tamaño de la población máxima")
        else:
            self.dialogoDeMensaje("El tamaño de la población inicial no puede ser 0, introduzca un valor mayor a 0")

    def dialogoDeMensaje(self, texto:str):
        msg = QMessageBox()
        msg.setText(texto)
        msg.setWindowTitle("Information")
        msg.exec_()

    
if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = Window()
    demo.show()

    try: 
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')