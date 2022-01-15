#import libraries PyQt5
#import the name of the file from designer 
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic 


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./Views/main.ui', self)
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Window()
    demo.show()

    try: 
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')