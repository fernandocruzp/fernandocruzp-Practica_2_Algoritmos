import simpy
from Nodo import *
from Canales.CanalBroadcast import *

TICK = 1

class NodoGenerador(Nodo):
    '''Implementa la interfaz de Nodo para el algoritmo de flooding.'''
    def __init__(self, id_nodo, vecinos, canal_entrada, canal_salida):
        '''Inicializamos el nodo.'''
        self.id_nodo = id_nodo
        self.vecinos = vecinos
        self.canal_entrada = canal_entrada
        self.canal_salida = canal_salida
        
        # Atributos propios del algoritmo
        self.padre = None if id_nodo != 0 else id_nodo # Si es el nodo distinguido, el padre es el mismo 
        self.hijos = list()
        self.mensajes_esperados = len(vecinos) # Cantidad de mensajes que esperamos
    
    def genera_arbol(self, env):
        '''
        Si el nodo es el distinguido (id_nodo=0), envía un mensaje inicial a sus vecinos.
        Los nodos que reciben el mensaje, si no tienen padre asignado, adoptan el nodo remitente como padre
        y reenvían el mensaje "GO" a sus propios vecinos. Una vez que todos los vecinos han respondido, envían un mensaje "Back" a su padre.

        Parámetros:
            env (simpy.Environment): El entorno de simulación de SimPy.
        '''
        if self.id_nodo == 0:
            # El nodo distinguido envía un mensaje inicial "GO" a sus vecinos
            env.process(self.canal_salida.envia("GO," + str(self.id_nodo), self.vecinos))
        
        while True:
            mensaje_recibido = yield self.canal_entrada.get()
            mensaje = mensaje_recibido.split(",")
            accion = mensaje[0]
            id_recibido = int(mensaje[1]) if mensaje[1] != "None" else None

            if accion == "GO":
                if self.padre is None:
                    # Si el nodo no tiene padre, el nodo remitente se convierte en su padre
                    self.padre = id_recibido
                    self.mensajes_esperados -= 1 
                    if self.mensajes_esperados == 0:
                        # Si ya no espera más mensajes, envía un mensaje "Back" a su padre
                        env.process(self.canal_salida.envia("Back," + str(self.id_nodo), [self.padre]))
                    else:
                        # Reenvía "GO" a sus vecinos, excepto el padre
                        env.process(self.canal_salida.envia("GO," + str(self.id_nodo), [x for x in self.vecinos if x != self.padre]))
                else:
                    # Si ya tiene padre, responde con "Back" indicando que el nodo remitente no es su padre
                    env.process(self.canal_salida.envia("Back,None", [id_recibido]))

            elif accion == "Back":
                self.mensajes_esperados -= 1
                if id_recibido is not None:
                    # Si el mensaje "Back" proviene de un hijo, lo añade a la lista de hijos
                    self.hijos.append(id_recibido)
                if self.mensajes_esperados == 0 and self.padre is not None:
                    # Si ya no espera mensajes y tiene padre, envía "Back" a su padre
                    if self.id_nodo != 0:
                        env.process(self.canal_salida.envia("Back," + str(self.id_nodo), [self.padre]))

            yield env.timeout(TICK)
