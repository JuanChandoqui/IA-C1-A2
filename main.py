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
        

    def iniciarAlgoritmo(self):
       
        print('BOTON DE INICIAR ALGORITMO....')
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

        if (tamPobIni > 0):
            if(tamPobIni <= tamPobMax):
                if(numIteraciones > 0):
                    if(self.radioButton_Maximizar.isChecked() != False or self.radioButton_Minimizar.isChecked() != False):
                        if self.radioButton_Maximizar.isChecked():
                            opcion = 0
                            Poblacion(tamPobIni, tamPobMax, resolucionX, resolucionY, rangoXmin, rangoXmax, rangoYmin, rangoYmax, probMutacionInd, probMutacionGen, numIteraciones, opcion)
                        elif self.radioButton_Minimizar.isChecked():      
                            opcion = 1
                            Poblacion(tamPobIni, tamPobMax, resolucionX, resolucionY, rangoXmin, rangoXmax, rangoYmin, rangoYmax, probMutacionInd, probMutacionGen, numIteraciones, opcion)
                    else: 
                        self.dialogoDeMensaje("Elige una opción de gráfica: Maximizar o minimizar")
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