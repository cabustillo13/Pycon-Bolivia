# Pycon-Bolivia
Una serie de juegos para la difusión del gran evento Pycon Bolivia 2020.

## Objetivo del proyecto

Se plantea la _Gamificación_, busca aumentar la motivación de los participantes a priori en entornos que no son lúdicos y así alcancar los mejores resultados. Con los juegos de esta repo, se busca aprender sobre las actividades de la Pycon Bolivia y también aprender técnicas de Python en el proceso.

## Juego 3: Trivia Game

Este juego es ideal para aprender mediante preguntas y respuestas, diferentes datos sobre los expositores y actividades de la Pycon. Siempre se puede aprender algo nuevo. Para este caso se puede ejecutar el ejecutable ```Game``` de la carpeta _juego3_. Es un juego hecho con la librería Pygame.

[![Ver Demo](https://github.com/cabustillo13/Pycon-Bolivia/blob/master/Recursos/portada.png)](https://youtu.be/PBkFbsfmMw4)

## Juego 2: ¿Cuántos logos hay en la imagen?

Es un juego para contar la mayor cantidad de logos en el menor tiempo posible. El juego se vuelve complejo conforme aumenta la cantidad de logos por imagen y una disminución del tiempo. Puedes realizar este proceso de manera automática con la ayuda del _Template Matching_ ejecutando el script ```juego2.py```.

Remarca los objetos detectados pasados como referencia. Y por terminal devuelve cuántos objetos encuentra. 
Sí te interesa agregar complejidad al script: puedes colocar imágenes al azar para posteriormente analizarlas con el Template Matching, variar las imágenes de referencia por un factor de escala para hacerlo más dinámico, etc.

 <img src="https://github.com/cabustillo13/Pycon-Bolivia/blob/master/Recursos/comparacion2.png" height="300" width="750">

## Juego 1: Encuentra las diferencias
¿Eres capaz de encontrar las diferencias que exiten entre ambas imágenes? 

Una manera de resolver este tipo de juego es utilizando el _Índice de Similitud Estructural_ en Python, para resaltar cambios entre dos imágenes.

Intenta encontrar las diferencias vos mismo, y después aplica el script ```juego1.py``` para comparar respuestas.

 <img src="https://github.com/cabustillo13/Pycon-Bolivia/blob/master/Recursos/comparacion.png" height="300" width="750">
 
 # Recursos
 
 -Las imágenes son propiedad de [Pycon Bolivia](https://www.facebook.com/pyconbolivia) y [PyLadies Cochabamba](https://www.facebook.com/PyladiesCbba).
 
 -Los sonidos fueron obtenidos de [Freesound.org](https://freesound.org) cuyos recursos presentan licencia Creative Commons CC BY-NC 3.0.
 
 -Para el juego de TriviaGame me base en el juego [guadaquiz](https://github.com/guadalinex-archive/guadaquiz) que presenta una licencia GPL.
 
 # Licencia
 Este proyecto esta bajo Licence (MIT).
