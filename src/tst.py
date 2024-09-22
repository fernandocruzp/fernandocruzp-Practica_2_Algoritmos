import simpy
from NodoConvergecast import NodoConvergecast  # Importamos el NodoConvergecast
from Canales.CanalConvergecast import CanalConvergecast  # Importamos el CanalConvergecast

# creando el entorno de Simpy
env = simpy.Environment()

# creando el canal de comunicación
canal = CanalConvergecast(env, capacidad=10)

# construyendo los nodos
nodo0 = NodoConvergecast(0, [], canal.crea_canal_de_entrada(0), canal.crea_canal_de_entrada(0), es_raiz=True)
nodo1 = NodoConvergecast(1, [nodo0], canal.crea_canal_de_entrada(1), canal.crea_canal_de_entrada(1))
nodo2 = NodoConvergecast(2, [nodo0], canal.crea_canal_de_entrada(2), canal.crea_canal_de_entrada(2))
nodo3 = NodoConvergecast(3, [nodo1, nodo2], canal.crea_canal_de_entrada(3), canal.crea_canal_de_entrada(3))
nodo4 = NodoConvergecast(4, [nodo1], canal.crea_canal_de_entrada(4), canal.crea_canal_de_entrada(4))
nodo5 = NodoConvergecast(5, [nodo2], canal.crea_canal_de_entrada(5), canal.crea_canal_de_entrada(5))

# ejecutando el proceso de convergecast para cada nodo
env.process(nodo1.ejecutar_convergecast(env, canal))
env.process(nodo2.ejecutar_convergecast(env, canal))
env.process(nodo3.ejecutar_convergecast(env, canal))
env.process(nodo4.ejecutar_convergecast(env, canal))
env.process(nodo5.ejecutar_convergecast(env, canal))
env.process(nodo0.ejecutar_convergecast(env, canal))  # la raíz también ejecuta su proceso

# simulando.
env.run()
