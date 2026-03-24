# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import time
import random
from game import Directions

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]

def depthFirstSearch(problema):#Modificado DFC
    tiempo_inicio = time.time() 
    pila = util.Stack()  #usa pila 
    inicio = [problema.getStartState(), 0, []]  
    pila.push(inicio)       
    explorados = [] #lista explorados
    
    while not pila.isEmpty():   #mientras tenga que explorar
        [estado_actual, costo_actual, camino_actual] = pila.pop()  #extrae ultimo nodo
        
        if problema.isGoalState(estado_actual): #objetivo
            tiempo_fin = time.time()            
            tiempo_transcurrido = tiempo_fin - tiempo_inicio
            print(f"Tiempo de búsqueda: {tiempo_transcurrido:.6f} segundos")
            return camino_actual  #camino solucion
        
        if not estado_actual in explorados:  #no explorado
            explorados.append(estado_actual)  #marca explorado
            
            for estado_hijo, accion_hijo, costo_hijo in problema.getSuccessors(estado_actual):
                nuevo_costo = costo_actual + costo_hijo  
                nuevo_camino = camino_actual + [accion_hijo]  #construye nuevo camino
                pila.push([estado_hijo, nuevo_costo, nuevo_camino])  #agrega a la pila


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problema, heuristic=nullHeuristic):#modificado BAE
    tiempo_inicio = time.time()  
    pila = util.PriorityQueue()  
    inicio = [problema.getStartState(), 0, []]  
    prioridad = 0
    pila.push(inicio, prioridad) 
    explorados = []  #lista explorados
    
    while not pila.isEmpty():  #mientras tenga que explorar
        [estado_actual, costo_actual, camino_actual] = pila.pop()
        
        if problema.isGoalState(estado_actual):  #objetivo
            tiempo_fin = time.time()
            tiempo_transcurrido = tiempo_fin - tiempo_inicio
            print(f"Tiempo total: {tiempo_transcurrido:.6f} segundos")
            return camino_actual  #camino solucion
            
        if estado_actual not in explorados:  #no explorado
            explorados.append(estado_actual)  #marca explorado
            
            for estado_hijo, accion_hijo, costo_hijo in problema.getSuccessors(estado_actual):
                nuevo_costo = costo_actual + costo_hijo
                nuevo_camino = camino_actual + [accion_hijo]
                
                prioridad = nuevo_costo + heuristic(estado_hijo, problema)
                pila.push([estado_hijo, nuevo_costo, nuevo_camino], prioridad)


def Siguienteposicion(posicion, accion):
    dx = 0 
    dy = 0
    if accion == Directions.NORTH:
        dy = 1
    elif accion == Directions.SOUTH:
        dy = -1
    elif accion == Directions.EAST:
        dx = 1
    elif accion == Directions.WEST:
        dx = -1
    
    return (posicion[0] + dx, posicion[1] + dy)

def retroceder(accion):
    if accion == Directions.NORTH:
        return Directions.SOUTH
    elif accion == Directions.SOUTH:
        return Directions.NORTH
    elif accion == Directions.EAST:
        return Directions.WEST
    elif accion == Directions.WEST:
        return Directions.EAST

def exploracion(estado, visitadas, pila):
    posicion_actual = estado.getPacmanPosition()
    visitadas[posicion_actual] = True
    acciones_legales = estado.getLegalPacmanActions()  
    acciones_no_exploradas = []
    
    for accion in acciones_legales:
        if accion == Directions.STOP:
            continue

        siguiente_pos = Siguienteposicion(posicion_actual, accion)

        if siguiente_pos not in visitadas:
            acciones_no_exploradas.append(accion)
    
    if acciones_no_exploradas:
        accion_elegida = random.choice(acciones_no_exploradas)
        pila.append(accion_elegida)
        return accion_elegida
    
    else:
        if pila:
            ultima_accion = pila.pop()
            accion_retroceso = retroceder(ultima_accion)

            if accion_retroceso in acciones_legales:
                return accion_retroceso
            else:
                return Directions.STOP
            
        else:
            return Directions.STOP

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch