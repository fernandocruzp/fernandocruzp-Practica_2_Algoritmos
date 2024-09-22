from Canales.Canal import Canal
import simpy

class CanalConvergecast(Canal):
    # inicializando canal.
    def __init__(self, env: simpy.Environment, capacidad: int):
        super().__init__(env, capacidad)
        self.env = env
        self.capacidad = capacidad
        self.canales_de_entrada = {}

    # metodo para crear un store con el id del nodo para recibir mensajes.
    def crea_canal_de_entrada(self, id_nodo: int):
        self.canales_de_entrada[id_nodo] = simpy.Store(self.env, capacity=self.capacidad)
        return self.canales_de_entrada[id_nodo]

    # metodo para enviar mensajes a los vecinos conectados.
    def envia(self, mensaje, vecinos):
        for vecino in vecinos:
            canal_entrada = self.canales_de_entrada[vecino.get_id()]  # Asegúrate de que vecino sea un Nodo
            if canal_entrada.capacity > len(canal_entrada.items):
                self.env.process(self._enviar_mensaje(vecino, canal_entrada, mensaje))

    # usando simpy para manejar el envío de mensajes de manera asincrónica.
    def _enviar_mensaje(self, vecino, canal_entrada, mensaje):    
        yield self.env.timeout(1)  # Simula un pequeño retraso en la transmisión
        print(f"Enviando mensaje al nodo {vecino.get_id()}: {mensaje}")
        yield canal_entrada.put(mensaje)
