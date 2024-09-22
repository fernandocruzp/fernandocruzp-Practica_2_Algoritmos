Cruz Pineda Fernando 423076479
Rodríguez Escobar David Yael 420088930
Sánchez Pavia Ángel Gabriel 318281940

Ejercicio 1

En el ejercicio 0 unicamente tuvimos que modificar primero la clase CanalBroadcast.py, en esta clase implementamos el método envía, que lo único que hace es con un for, enviar a cada uno de los vecinos el mensaje a través del canal establecido en la lista de canales.

Ejercicio 2

En el ejercicio 2, el nodo distinguido inicia el proceso enviando un mensaje "GO" a sus vecinos. Cada nodo que recibe este mensaje, si aún no tiene un padre asignado, se marca a sí mismo como hijo del nodo que le envió el mensaje y reenvía el mensaje "GO" a sus vecinos, excepto al nodo de quien recibió el mensaje (para evitar ciclos).

El nodo sigue esperando respuestas de sus vecinos. Cuando un nodo ha recibido las respuestas esperadas de todos sus vecinos (mensaje "Back"), envía un mensaje de confirmación "Back" a su padre, indicando que ya terminó de procesar sus vecinos. Si el nodo no tiene padre (nodo distinguido), el proceso concluye cuando ha recibido todas las confirmaciones de vuelta.

Ejercicio 3

Usamos la misma clase de CanalBroadcast.py que en el ejercicio 1.
Después implementamos el algoritmo de Broadcast, en éste primero vemos si somos el nodo distinguido con id 0, si ese es el caso, utilizando el canal de salida, envíamos a cada uno de nuestros vecinos el mensaje "hola". Si no es el nodo distinguido, entonces con un while True esperas a recibir un mensaje en tu canal de entrada, esto lo hacemos con yield, si no habías recibido mensaje antes, ese es tu nuevo mensaje y se lo envías a todos tus vecinos.
