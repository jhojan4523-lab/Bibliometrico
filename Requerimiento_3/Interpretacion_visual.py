import matplotlib.pyplot as plt
import os
from tqdm import tqdm
import networkx as nx
from wordcloud import WordCloud
from networkx.algorithms import community
import matplotlib.patheffects as path_effects
import pandas as pd
from collections import Counter
from itertools import combinations
import matplotlib.cm as cm
import numpy as np
import matplotlib.patches as mpatches


# Ruta donde se guardarán los gráficos
ruta_graficos = "C:/2025-2/day/algorit/Proyecto-algoritmos/Data/Datos Requerimiento3"


# Paso 4: Generar una gráfica de barras
def plot_bar_chart(keyword_counts):

    top_10 = sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)[:20]
    # Separar claves y valores
    keywords = [item[0] for item in top_10]
    counts = [item[1] for item in top_10]

    plt.figure(figsize=(12, 6))
    plt.barh(keywords, counts, color="skyblue")

    #Agregar etiquetas al final de la barra
    for i, count in enumerate(counts):
        plt.text(count + 0.5, i, str(count), va='center', fontsize=10)

    plt.xlabel("Frecuencia")
    plt.title("Top 20 - Frecuencia de Palabras Clave")
    plt.tight_layout()
    plt.savefig(os.path.join(ruta_graficos, "frecuencia_palabras_clave.png"))
    plt.close()

