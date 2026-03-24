# 🔍 Práctica 2 — Exploración y Búsqueda

Implementación de agentes inteligentes para el entorno Pacman, aplicando estrategias de **exploración** y **búsqueda** tanto no informada como informada.

---

## 📋 Actividades

| Actividad | Descripción |
|---|---|
| Actividad 1 | Implementación del agente explorador |
| Actividad 2 | Análisis del agente explorador |
| Actividad 3 | Agente con búsqueda en profundidad (DFS) |
| Actividad 4 | Agente con búsqueda informada A* (BAE) |
| Actividad 5 | Análisis comparativo DFS vs BAE |

---

## 🤖 Agentes implementados

### `AgentePropio` — Agente Explorador

**Archivo:** `searchAgents.py` | **Función auxiliar:** `exploracion()` en `search.py`

El agente explorador recorre el laberinto intentando visitar el mayor número posible de casillas únicas. Su estrategia se basa en un **DFS aleatorio con backtracking**:

- Mantiene un diccionario interno de `visitadas` para registrar las posiciones ya recorridas.
- En cada paso, obtiene las acciones legales disponibles y filtra aquellas que llevan a posiciones no visitadas.
- Si hay posiciones sin explorar accesibles, elige una **aleatoriamente** y la apila en su historial.
- Si no quedan posiciones nuevas, **retrocede** por el camino recorrido (backtracking) hasta encontrar un punto con ramas sin explorar.
- Al finalizar la partida imprime estadísticas: pasos totales, casillas únicas visitadas, ratio de repetición y tiempo transcurrido.

```bash
# Ejecutar el agente explorador
python pacman.py --layout smallMaze --pacman AgentePropio -k 0
python pacman.py --layout bigMaze --pacman AgentePropio -k 0 -z 0.5
```

---

### `AgentePropioDFS` — Búsqueda en Profundidad

**Archivo:** `searchAgents.py` | **Función:** `depthFirstSearch()` en `search.py`

Agente buscador que usa el algoritmo **DFS (Depth-First Search)** para encontrar un camino desde la posición inicial hasta el objetivo.

- Utiliza una **pila (Stack)** para gestionar los nodos a explorar (LIFO).
- Cada nodo almacena: estado actual, coste acumulado y camino recorrido.
- Mantiene una lista de nodos `explorados` para evitar ciclos (búsqueda en grafo).
- Devuelve el primer camino encontrado hasta el objetivo, que no tiene por qué ser el óptimo.
- Imprime el tiempo de búsqueda al encontrar la solución.

```bash
# Ejecutar el agente DFS
python pacman.py --layout testMaze --pacman AgentePropioDFS -k 0
python pacman.py --layout mediumMaze --pacman AgentePropioDFS -k 0
python pacman.py --layout bigMaze --pacman AgentePropioDFS -k 0 -z 0.5
```

---

### `AgentePropioBAE` — Búsqueda A* con Heurística Manhattan

**Archivo:** `searchAgents.py` | **Función:** `aStarSearch()` en `search.py`

Agente buscador que usa el algoritmo **A\* (BAE)** con la **heurística de distancia Manhattan** para encontrar el camino óptimo hasta el objetivo.

- Utiliza una **cola de prioridad (PriorityQueue)** donde la prioridad de cada nodo es `f(n) = g(n) + h(n)`:
  - `g(n)`: coste real acumulado desde el inicio.
  - `h(n)`: estimación heurística hasta el objetivo (distancia Manhattan).
- Mantiene una lista de nodos `explorados` para evitar reexpandir estados ya visitados.
- Garantiza una solución **completa y óptima** siempre que la heurística sea admisible.
- La distancia Manhattan calcula `|x1 - x2| + |y1 - y2|`, que es admisible en este entorno.
- Imprime el tiempo total de búsqueda al encontrar la solución.

```bash
# Ejecutar el agente A* (BAE)
python pacman.py --layout testMaze --pacman AgentePropioBAE -k 0
python pacman.py --layout mediumMaze --pacman AgentePropioBAE -k 0
python pacman.py --layout bigMaze --pacman AgentePropioBAE -k 0 -z 0.5
```

---

## ⚖️ Comparativa de agentes

| Característica | AgentePropio | AgentePropioDFS | AgentePropioBAE |
|---|---|---|---|
| Tipo | Exploración | Búsqueda no informada | Búsqueda informada |
| Estructura de datos | Pila (lista Python) | Stack | PriorityQueue |
| Solución óptima | No aplica | ❌ No garantizada | ✅ Garantizada |
| Usa heurística | ❌ | ❌ | ✅ Manhattan |
| Objetivo | Máxima cobertura | Llegar al goal | Llegar al goal (mínimo coste) |

---

## 🗺️ Laberintos recomendados para pruebas

```bash
# Laberintos sin fantasmas (-k 0)
python pacman.py --layout smallMaze      --pacman AgentePropioBAE -k 0
python pacman.py --layout mediumMaze     --pacman AgentePropioBAE -k 0
python pacman.py --layout bigMaze        --pacman AgentePropioBAE -k 0 -z 0.5
python pacman.py --layout bigSafeSearch  --pacman AgentePropioBAE -k 0 -z 0.5
python pacman.py --layout openMaze       --pacman AgentePropioBAE -k 0
python pacman.py --layout trickySearch   --pacman AgentePropioBAE -k 0

# Con fantasmas (entorno multi-agente)
python pacman.py --layout mediumMaze --pacman AgentePropioDFS
python pacman.py --layout mediumMaze --pacman AgentePropioBAE
```

---

## 📁 Archivos modificados

Solo se han modificado los siguientes archivos respecto al proyecto base:

- **`search.py`** — Implementación de `depthFirstSearch`, `aStarSearch` y `exploracion`.
- **`searchAgents.py`** — Implementación de `AgentePropio`, `AgentePropioDFS` y `AgentePropioBAE`.
