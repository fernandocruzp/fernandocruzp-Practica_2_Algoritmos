from Nodo import Nodo
import simpy

class NodoConvergecast(Nodo):
    def __init__(self, id_nodo, vecinos, canal_entrada, canal_salida, es_raiz=False):
        super().__init__(id_nodo, vecinos, canal_entrada, canal_salida)
        # inicializando nodoConvergecast
        self.id_nodo = id_nodo  
        self.vecinos = vecinos
        self.canal_entrada = canal_entrada
        self.canal_salida = canal_salida
        self.es_raiz = es_raiz
        self.mensaje_propio = f"Mensaje desde nodo {id_nodo}"
        self.mensajes_recibidos = []  # Almacenando los mensajes que el nodo ha recibido


    # metodo para devolver el id del nodo
    def get_id(self):
        return self.id_nodo

    # metodo para enviar mensajes a los vecinos (hacia arriba en la jerarquía).
    def enviar_mensaje(self, canal):
        if self.mensajes_recibidos:
            # Si ha recibido mensajes, envía su mensaje junto con los recibidos
            mensaje_a_enviar = f"{self.mensaje_propio} y {self.mensajes_recibidos}"
        else:
            mensaje_a_enviar = self.mensaje_propio

        print(f"El nodo {self.get_id()} envía su mensaje a sus vecinos.")
        canal.envia(mensaje_a_enviar, self.vecinos)

    # metodo para recibir mensajes de otro nodo
    def recibir_mensaje(self, mensaje):
        print(f"El nodo {self.get_id()} ha recibido el mensaje: {mensaje}")
        self.mensajes_recibidos.append(mensaje)  # Almacena el mensaje recibido

    # metodo para ejecutar el proceso principal (enviar y recibir mensajes)
    def ejecutar_convergecast(self, env, canal):
        yield env.timeout(2)  # Simulación del tiempo de ejecución
        if not self.es_raiz:
            # Si no es la raíz, envía su mensaje a sus vecinos (hacia la raíz)
            self.enviar_mensaje(canal)
        else:
            # Si es la raíz, recolecta mensajes
            print(f"El nodo {self.get_id()} es la raíz y recolecta mensajes.")
