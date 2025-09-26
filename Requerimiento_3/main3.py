from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import networkx as nx
import os
import sys
from tqdm import tqdm
import pandas as pd

# Agregar la carpeta raíz al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Requerimiento_3.Palabras import keywords
from Requerimiento_3.Interpretacion_visual import plot_bar_chart,  cargarPalabras_excel  
from Requerimiento_3.Analisis_abtract import parse_large_bib, load_bibtex, count_keywords, extract_new_terms

# Paso 6: Guardar resultados en un archivo Excel
def guardar_keywords_en_excel(keyword_data, output_path):
    df = pd.DataFrame(keyword_data)
    df = df.sort_values(by=["Categoría", "Frecuencia"], ascending=[True, False])
    df.to_excel(output_path, index=False)

# Paso 7: Integrar todo el flujo
def main(bib_file_path):
    try:
        # Cargar abstracts
        abstracts = load_bibtex(bib_file_path)
        
        if not abstracts:
            print("Advertencia: No se encontraron abstracts en el archivo.")
            print("Verifica que los campos 'abstract' existan en las entradas .bib")
            return
        
        # Contar palabras clave
        keyword_data, keyword_counts = count_keywords(abstracts, keywords)

        # Descubrimiento de nuevas palabras
        new_terms = extract_new_terms(abstracts, keywords, top_n=15)

        # Convertir a DataFrame
        df_new_terms = pd.DataFrame(new_terms, columns=["Término", "Frecuencia"])
        
        if not keyword_counts:
            print("Advertencia: No se encontraron coincidencias con las palabras clave.")
            print("Verifica que los abstracts contengan los términos buscados.")
            return
        
        # Mostrar resultados
        print("\nFrecuencias de Palabras Clave:")
        for keyword, count in sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"{keyword}: {count}")

        # Guardar resultados en Excel
        output_excel = os.path.join(ruta_graficos, "frecuencia_keywords_categorizadas.xlsx")
        guardar_keywords_en_excel(keyword_data, output_excel)
        print(f"Archivo Excel guardado en: {output_excel}")

        excel_path = "C:/2025-2/day/algorit/Proyecto-algoritmos/Data/Datos Requerimiento3/frecuencia_keywords_categorizadas.xlsx"

        # Guardar en Excel
        output_excel = "C:/2025-2/day/algorit/Proyecto-algoritmos/Data/Datos Requerimiento3/nuevas_palabras.xlsx"
        df_new_terms.to_excel(output_excel, index=False)

        print(f"Nuevas palabras asociadas a terminos guardadas en: {output_excel}")

        # Cargar palabras clave desde el archivo Excel
        keywords_by_category = cargarPalabras_excel(excel_path)

        # Graficar resultados
        plot_bar_chart(keyword_counts)
        generate_wordcloud(keyword_counts)
        plot_cooccurrence_network(keywords_by_category)
        
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    bib_file_path = "C:/2025-2/day/algorit/Proyecto-algoritmos/Data/unificados.bib"
    ruta_graficos = "C:/2025-2/day/algorit/Proyecto-algoritmos/Data/Datos Requerimiento3"
    
    # Ejecutar el flujo principal
    main(bib_file_path)
    print(f"Análisis de palabras clave completado. Gráficos guardados en {ruta_graficos}.")