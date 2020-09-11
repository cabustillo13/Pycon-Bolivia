import cv2
import numpy as np
from matplotlib import pyplot as plt

# Imagen a analizar
imagenColor = cv2.imread('./Recursos/juego2/photo0.png')
imagenGris = cv2.cvtColor(imagenColor, cv2.COLOR_BGR2GRAY)

cont=0      #Cantidad de rectangulos
tol=5       #Tolerancia para evitar duplicado en el conteo de rectangulos

# Plantillas a detectar
for i in range(3):
    path = './Recursos/juego2/ref' + str(i) +'.png'
    template = cv2.imread(path,0)
    w, h = template.shape[::-1]

    # Plantilla de comparacion
    res = cv2.matchTemplate(imagenGris,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)

    listPt=list()
    #Detectar y dibujar rectangulos
    for pt in zip(*loc[::-1]):
        cv2.rectangle(imagenColor, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        listPt.append(([pt[0],pt[1]]))
        
    #Contar rectangulos
    listPt.sort()
    for i in range (len(listPt)-1):
        valor = abs(listPt[i+1][1] - listPt[i][1]) + abs(listPt[i+1][0] - listPt[i][0])
        if (valor > tol) or (i==0):
            cont+=1
        
#Mostrar y guardar resultados    
cv2.imwrite("./Recursos/juego2/ejemplo.png",imagenColor)
print("Cantidad de rectangulos detectados: ",cont)

#Bibliografia: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html 
