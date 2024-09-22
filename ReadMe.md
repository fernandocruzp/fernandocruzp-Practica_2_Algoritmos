Cruz Pineda Fernando 423076479



Ejercicio 1

En el ejercicio 0 unicamente tuvimos que modificar primero la clase CanalBroadcast.py, en esta clase implementamos el método envía, que lo único que hace es con un for, enviar a cada uno de los vecinos el mensaje a través del canal establecido en la lista de canales.

Ejercicio 2

Ejercicio 3

Usamos la misma clase de CanalBroadcast.py que en el ejercicio 1.
Después implementamos el algoritmo de Broadcast, en éste primero vemos si somos el nodo distinguido con id 0, si ese es el caso, utilizando el canal de salida, envíamos a cada uno de nuestros vecinos el mensaje "hola". Si no es el nodo distinguido, entonces con un while True esperas a recibir un mensaje en tu canal de entrada, esto lo hacemos con yield, si no habías recibido mensaje antes, ese es tu nuevo mensaje y se lo envías a todos tus vecinos.
