# Practica2_SISIN

Se pide encontrar la manera de trasladar a los misioneros y a los caníbales a la otra orilla del río, con la condición de que en ningún momento quede en contacto un número de misioneros con un número mayor de caníbales.  La dificultad reside en que, si la condición mencionada no se cumple, alguno de los misioneros es devorado y no se puede alcanzar el objetivo del juego. ¿Cuál es la solución menos costosa para este problema?

![alt text](https://miro.medium.com/max/829/1*lrYS8lSDLJdUGCmgnCxkTg.png "Misioneros y canívales")

* Representar el espacio de problemas (Asumo que se refiere al espacio de estados del problema)

  Para el estado inicial se asume que hay 3 misioneros del lado incorrecto, 3 canívales del lado incorrecto y el bote también está del lado         incorrecto:

  Descripción | Misioneros | Canívales | Bote
  --- | :---: | :---: | :---:
  Estado Inicial | 3 | 3 | 1
  
  Por lo tanto, la solución estaría dada cuando el estado sea (0,0,0)
  
  El espacio de estados válidos para el primer paso de la solución sería el siguiente:
  
  Descripción | Misioneros | Canívales | Bote
  --- | :---: | :---: | :---:
  Mover 2 canívales | 3 | 1 | 0
  Mover 1 misionero | 2 | 2 | 0
  Mover 1 caníval | 3 | 2 | 0
  
  Se descarta el estado (3,2,0), ya que para continuar el caníval debe regresar, resultando en una redundancia.
  
  Sea el estado (3,1,0) ó (2,2,0), el siguiente estado será el mismo:
  
  Descripción | Misioneros | Canívales | Bote
  --- | :---: | :---: | :---:
  Mover 1 caníval de regreso | 3 | 2 | 1
  Mover 1 misionero de regreso | 3 | 2 | 1
  
  Luego:
  
  Descripción | Misioneros | Canívales | Bote
  --- | :---: | :---: | :---:
  Mover 2 canívales | 3 | 0 | 0
  
  Luego:
  
  Descripción | Misioneros | Canívales | Bote
  --- | :---: | :---: | :---:
  Mover 1 caníval de regreso | 3 | 1 | 1
  
  Luego:
  
  Descripción | Misioneros | Canívales | Bote
  --- | :---: | :---: | :---:
  Mover 2 misioneros | 1 | 1 | 0
  
  Luego:
  
  Descripción | Misioneros | Canívales | Bote
  --- | :---: | :---: | :---:
  Mover 1 caníval y 1 misionero de regreso | 2 | 2 | 1
  
  Luego:
  
  Descripción | Misioneros | Canívales | Bote
  --- | :---: | :---: | :---:
  Mover 2 misioneros | 0 | 2 | 0
  
  Luego:
  
  Descripción | Misioneros | Canívales | Bote
  --- | :---: | :---: | :---:
  Mover 1 caníval de regreso | 0 | 3 | 1
  
  Luego:
  
  Descripción | Misioneros | Canívales | Bote
  --- | :---: | :---: | :---:
  Mover 2 canívales | 0 | 1 | 0
  
  Luego se tienen 2 opciones:
  
  Descripción | Misioneros | Canívales | Bote
  --- | :---: | :---: | :---:
  Mover 1 caníval de regreso | 0 | 2 | 1
  Mover 1 misionero de regreso | 1 | 1 | 1
  
  Por último:
  
  Descripción | Misioneros | Canívales | Bote
  --- | :---: | :---: | :---:
  En el estado (0,2,1), mover 2 canívales | 0 | 0 | 0
  En el estado (1,1,1), mover 1 caníval y 1 misionero | 0 | 0 | 0
