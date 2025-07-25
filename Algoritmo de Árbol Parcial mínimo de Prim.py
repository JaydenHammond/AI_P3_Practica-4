# -*- coding: utf-8 -*-
"""
Practica - 4 Algoritmo de Árbol Parcial mínimo de Prim
Jayden Hammond Caballero - 22310235
"""
# =============================================================================
# #f5 Para ejecutar
# =============================================================================
# Simulador de rutas de entrega con el Algoritmo de Árbol Parcial mínimo de Prim
# Estaciones de bicicletas

import heapq
import matplotlib.pyplot as plt
import networkx as nx

# MAPA
estaciones = {
    'Estación Central': {'Parque Norte': 4, 'Mercado': 2},
    'Parque Norte': {'Estación Central': 4, 'Universidad': 3, 'Hospital': 7},
    'Mercado': {'Estación Central': 2, 'Universidad': 6, 'Biblioteca': 3},
    'Universidad': {'Parque Norte': 3, 'Mercado': 6, 'Hospital': 5, 'Biblioteca': 4},
    'Hospital': {'Parque Norte': 7, 'Universidad': 5, 'Biblioteca': 6},
    'Biblioteca': {'Mercado': 3, 'Universidad': 4, 'Hospital': 6}
}

# ALGORITMO
def prim_mst(graph, start):
    mst = []
    visited = set()
    edges = [(weight, start, neighbor) for neighbor, weight in graph[start].items()]
    heapq.heapify(edges)
    pasos = []

    visited.add(start)

    while edges:
        weight, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))
            pasos.append((frm, to, weight))

            for neighbor, cost in graph[to].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (cost, to, neighbor))
    
    return mst, pasos

# PASOS
def mostrar_pasos(pasos):
    for i, (u, v, w) in enumerate(pasos):
        print(f"Paso {i+1}: Conectando '{u}' con '{v}' (Distancia: {w} km)")

# GRAFICAR
def graficar_mst(graph, mst_edges):
    G = nx.Graph()
    pos = nx.spring_layout(graph, seed=15)

    for lugar, conexiones in graph.items():
        for destino, peso in conexiones.items():
            G.add_edge(lugar, destino, weight=peso)

    nx.draw_networkx_nodes(G, pos, node_size=750, node_color='skyblue')
    nx.draw_networkx_labels(G, pos, font_weight='bold')
    nx.draw_networkx_edges(G, pos, edge_color='lightgray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))

    mst_edges_fmt = [(u, v) for u, v, _ in mst_edges]
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges_fmt, edge_color='green', width=3)

    plt.title("Estaciones de Bicicletas")
    plt.axis('off')
    plt.show()


# RESULTADOS
if __name__ == "__main__":
    nodo_inicio = 'Estación Central'
    mst_resultado, pasos = prim_mst(estaciones, nodo_inicio)

    print(f"\n Guia de Conexión entre Estaciones de Bicicletas\nInicio en: {nodo_inicio}\n")
    mostrar_pasos(pasos)

    print("\n Aristas del Árbol de Expansión Mínima:")
    for u, v, w in mst_resultado:
        print(f"{u} - {v} (Distancia: {w} km)")

    graficar_mst(estaciones, mst_resultado)
