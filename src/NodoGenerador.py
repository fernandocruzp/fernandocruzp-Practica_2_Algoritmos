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
        if self.id_nodo==0:
            env.process(self.canal_salida.envia("GO,"+ str(self.id_nodo), self.vecinos))
        
        while True:
            mensaje_recibido = yield self.canal_entrada.get()
            mensaje=mensaje_recibido.split(",")
            accion=mensaje[0]
            id_recibido=int(mensaje[1]) if mensaje[1] != "None" else None
            if accion == "GO":
                if self.padre is None:
                    self.padre = id_recibido
                    self.mensajes_esperados -=1 
                    if self.mensajes_esperados==0:
                        env.process(self.canal_salida.envia("Back,"+str(self.id_nodo), [self.padre]))
                    else:
                        env.process(self.canal_salida.envia("GO,"+str(self.id_nodo), [x for x in self.vecinos if x != self.padre]))
                else:
                    env.process(self.canal_salida.envia("Back,None", [id_recibido]))
            if accion == "Back":
                self.mensajes_esperados -=1
                if id_recibido is not None:
                    self.hijos.append(id_recibido)
                if self.mensajes_esperados == 0 and self.padre is not None:
                    if self.id_nodo != 0:
                        env.process(self.canal_salida.envia("Back,"+str(self.id_nodo), [self.padre]))
            yield env.timeout(TICK)
