# 🟡 Pacman-IA

Proyecto de Inteligencia Artificial basado en el entorno **Pacman** de UC Berkeley, desarrollado para la asignatura de Inteligencia Artificial de la Universidad de Jaén (Curso 2025/2026).

El agente Pacman navega por laberintos aplicando distintas estrategias de **exploración** y **búsqueda** para alcanzar objetivos de la forma más eficiente posible.

---

## 📁 Estructura del repositorio

```
Pacman-IA/
├── search.py            # Algoritmos de búsqueda (DFS, BFS, A*, exploración)
├── searchAgents.py      # Agentes que utilizan los algoritmos anteriores
├── pacman.py            # Lógica principal del juego
├── game.py              # Motor del juego (Agent, Directions, Grid...)
├── util.py              # Estructuras de datos (Stack, Queue, PriorityQueue)
├── ghostAgents.py       # Comportamiento de los fantasmas
├── pacmanAgents.py      # Agentes de ejemplo incluidos con el proyecto
├── layouts/             # Laberintos disponibles
├── Practica2/
│   └── README.md        # Documentación específica de la Práctica 2
└── README.md            # Este archivo
```

---

## ⚙️ Requisitos

- Python 3.6 o superior
- Sin dependencias externas — solo módulos estándar de Python

---

## 🚀 Ejecución

### Partida básica

```bash
python pacman.py
```

### Cambiar el laberinto

```bash
python pacman.py --layout nombreLayout
```

### Usar un agente concreto

```bash
python pacman.py --layout nombreLayout --pacman nombreAgente
```

### Sin fantasmas (recomendado para pruebas)

```bash
python pacman.py --layout nombreLayout --pacman nombreAgente -k 0
```

### Reducir el zoom en mapas grandes

```bash
python pacman.py --layout bigMaze --pacman nombreAgente -k 0 -z 0.5
```

### Ver todas las opciones disponibles

```bash
python pacman.py -h
```

---

## 🗺️ Laberintos disponibles

Algunos de los layouts incluidos en `layouts/`:

| Layout | Descripción |
|---|---|
| `testMaze` | Laberinto mínimo para pruebas rápidas |
| `smallMaze` | Laberinto pequeño |
| `mediumMaze` | Laberinto de tamaño medio |
| `bigMaze` | Laberinto grande |
| `openMaze` | Espacio abierto, pocas paredes |
| `originalClassic` | Mapa clásico de Pacman |
| `trickySearch` | Laberinto con caminos engañosos |
| `bigSafeSearch` | Laberinto grande sin fantasmas |

---

## 🤖 Agentes implementados

| Agente | Descripción |
|---|---|
| `AgentePropio` | Agente explorador con backtracking aleatorio |
| `AgentePropioDFS` | Agente buscador con búsqueda en profundidad (DFS) |
| `AgentePropioBAE` | Agente buscador con A* y heurística Manhattan |

Consulta la documentación específica de cada práctica para más detalles sobre su funcionamiento.

---

## 📚 Prácticas

| Práctica | Contenido |
|---|---|
| [Práctica 2](./Practica2/README.md) | Exploración y búsqueda — Agente explorador, DFS y A* |

---

## 🏫 Créditos

- Entorno Pacman original: [UC Berkeley AI Projects](http://ai.berkeley.edu)
- Adaptación y agentes implementados: Universidad de Jaén, asignatura Inteligencia Artificial
