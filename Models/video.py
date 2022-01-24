import os
import cv2
def generarVideo():
    #Ubicación de la base de datos
    path = './Resources/Images/'
    archivos = sorted([ int(i.replace('.png','')) for i in os.listdir(path)])
    print(sorted([ int(i.replace('.png','')) for i in os.listdir(path)]))
    img_array = []

    #Leer imagenes
    for x in range (0,len(archivos)):
        nomArchivo = str(archivos[x])+str('.png')
        dirArchivo = path + str(nomArchivo)
        img = cv2.imread(dirArchivo)
        img_array.append(img)
        
    #Dimensiones de los frames alto y ancho
    height, width  = img.shape[:2]

    #Caracteríasticas video
    video = cv2.VideoWriter('./Resources/Video/CVC-08.avi', cv2.VideoWriter_fourcc(*'DIVX'), 5, (width,height))

    #Colocar los frames en video
    for i in range(0, len(archivos)):
        video.write(img_array[i])
        
    #liberar
    video.release()                                                           
