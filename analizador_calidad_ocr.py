#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analizador de Calidad OCR - Periódicos Madrileños (1849-1939)
Proyecto LexiMus USAL - PID2022-139589NB-C33

Análisis sistemático de errores de OCR en 8 periódicos históricos
digitalizados por la Hemeroteca de la BNE.
"""

import os
import re
import json
from collections import defaultdict, Counter
import random

# Ruta base
BASE_DIR = "/Users/maria/Desktop/Periódicos COMPLETOS Hemeroteca BNE"

# Definición de periódicos
PERIODICOS = {
    "Crisol": {"carpeta": "Crisol", "periodo": "1931-1932"},
    "El Heraldo de Madrid": {"carpeta": "El Heraldo de Madrid", "periodo": "1890-1939"},
    "El Imparcial": {"carpeta": "El Imparcial", "periodo": "1867-1933"},
    "El Liberal": {"carpeta": "El Liberal", "periodo": "1879-1939"},
    "El Sol": {"carpeta": "El Sol", "periodo": "1917-1939"},
    "La Epoca": {"carpeta": "La Epoca", "periodo": "1849-1936"},
    "La Libertad": {"carpeta": "La Libertad", "periodo": "1919-1939"},
    "LA NACIÓN": {"carpeta": "LA NACIÓN", "periodo": "1925-1936"}
}

class AnalizadorCalidadOCR:
    def __init__(self):
        self.resultados = {}
        self.errores_comunes = defaultdict(int)
        self.estadisticas_globales = {
            "total_archivos_analizados": 0,
            "total_lineas_analizadas": 0,
            "total_palabras_analizadas": 0
        }

    def detectar_errores_ocr(self, texto):
        """
        Detecta patrones típicos de errores OCR.
        Devuelve dict con tipos de errores y sus frecuencias.
        """
        errores = {
            "caracteres_raros": 0,
            "numeros_en_palabras": 0,
            "mayusculas_aleatorias": 0,
            "espacios_ausentes": 0,
            "puntuacion_erronea": 0,
            "letras_confundidas": 0,
            "lineas_fragmentadas": 0,
            "texto_ilegible": 0
        }

        # Patrón 1: Caracteres raros y no-alfabéticos en palabras
        errores["caracteres_raros"] = len(re.findall(r'\w*[^\w\sáéíóúüñÁÉÍÓÚÜÑ¿¡.,;:()«»"\'`\-]\w*', texto))

        # Patrón 2: Números mezclados con letras (ej: "l3s", "5u", "0bra")
        errores["numeros_en_palabras"] = len(re.findall(r'\b\w*\d+\w*\b', texto))

        # Patrón 3: Mayúsculas aleatorias en medio de palabras
        errores["mayusculas_aleatorias"] = len(re.findall(r'\b\w+[a-z][A-Z]\w+\b', texto))

        # Patrón 4: Palabras pegadas (más de 25 caracteres sin espacios)
        errores["espacios_ausentes"] = len(re.findall(r'\b\w{25,}\b', texto))

        # Patrón 5: Puntuación múltiple o errónea
        errores["puntuacion_erronea"] = len(re.findall(r'[.,;:]{2,}|[^\w\s]{3,}', texto))

        # Patrón 6: Confusiones comunes (l/I, 0/O, rn/m, etc.)
        confusiones = [
            r'\bl[a-z]{1,2}\b',  # "la" como "Ia", "le" como "Ie"
            r'\b[Il]1\w+',        # I1, l1 al inicio
            r'\w*[Il]1\w*',       # I1, l1 en medio
            r'\b[O0][a-z]+',      # 0a, 0e (debería ser Oa, Oe)
        ]
        for patron in confusiones:
            errores["letras_confundidas"] += len(re.findall(patron, texto))

        # Patrón 7: Líneas muy cortas (fragmentación)
        lineas = texto.split('\n')
        errores["lineas_fragmentadas"] = sum(1 for l in lineas if 0 < len(l.strip()) < 10)

        # Patrón 8: Porcentaje de texto potencialmente ilegible
        palabras = texto.split()
        if palabras:
            palabras_sospechosas = sum(1 for p in palabras if len(re.findall(r'[^\w\sáéíóúüñÁÉÍÓÚÜÑ]', p)) > len(p)/3)
            errores["texto_ilegible"] = palabras_sospechosas

        return errores

    def analizar_archivo(self, ruta_archivo):
        """Analiza un archivo TXT y devuelve estadísticas de calidad OCR."""
        try:
            with open(ruta_archivo, 'r', encoding='utf-8', errors='ignore') as f:
                contenido = f.read()

            # Estadísticas básicas
            lineas = [l for l in contenido.split('\n') if l.strip()]
            palabras = contenido.split()

            # Detectar errores
            errores = self.detectar_errores_ocr(contenido)

            # Calcular métricas de calidad
            total_caracteres = len(contenido)
            total_errores = sum(errores.values())
            tasa_error = (total_errores / len(palabras) * 100) if palabras else 0

            return {
                "archivo": os.path.basename(ruta_archivo),
                "lineas": len(lineas),
                "palabras": len(palabras),
                "caracteres": total_caracteres,
                "errores": errores,
                "total_errores": total_errores,
                "tasa_error_porcentaje": round(tasa_error, 2),
                "calidad_estimada": self.estimar_calidad(tasa_error)
            }
        except Exception as e:
            print(f"Error analizando {ruta_archivo}: {str(e)}")
            return None

    def estimar_calidad(self, tasa_error):
        """Estima calidad del OCR basándose en tasa de error."""
        if tasa_error < 5:
            return "Excelente"
        elif tasa_error < 15:
            return "Buena"
        elif tasa_error < 30:
            return "Regular"
        elif tasa_error < 50:
            return "Mala"
        else:
            return "Muy mala"

    def seleccionar_muestras(self, carpeta, num_muestras=5):
        """
        Selecciona muestras estratificadas: inicio, medio, final del periodo
        y algunas aleatorias.
        """
        ruta = os.path.join(BASE_DIR, carpeta)
        archivos = sorted([f for f in os.listdir(ruta) if f.endswith('.txt')])

        if not archivos:
            return []

        total = len(archivos)
        indices = [
            0,                          # Primer archivo
            total // 4,                 # Primer cuarto
            total // 2,                 # Mitad
            (3 * total) // 4,           # Tercer cuarto
            total - 1                   # Último archivo
        ]

        # Añadir algunas muestras aleatorias adicionales
        if total > 10:
            aleatorios = random.sample(range(1, total-1), min(5, total-2))
            indices.extend(aleatorios)

        muestras = [os.path.join(ruta, archivos[i]) for i in sorted(set(indices))]
        return muestras[:num_muestras * 2]  # Máximo 10 muestras por periódico

    def analizar_periodico(self, nombre, info):
        """Analiza todas las muestras de un periódico."""
        print(f"\n{'='*60}")
        print(f"Analizando: {nombre} ({info['periodo']})")
        print(f"{'='*60}")

        muestras = self.seleccionar_muestras(info['carpeta'], num_muestras=5)
        resultados_muestras = []

        for muestra in muestras:
            print(f"  Procesando: {os.path.basename(muestra)}")
            resultado = self.analizar_archivo(muestra)
            if resultado:
                resultados_muestras.append(resultado)
                self.estadisticas_globales["total_archivos_analizados"] += 1
                self.estadisticas_globales["total_lineas_analizadas"] += resultado["lineas"]
                self.estadisticas_globales["total_palabras_analizadas"] += resultado["palabras"]

        # Calcular promedios
        if resultados_muestras:
            promedio_tasa_error = sum(r["tasa_error_porcentaje"] for r in resultados_muestras) / len(resultados_muestras)
            promedio_errores = {
                tipo: sum(r["errores"][tipo] for r in resultados_muestras) / len(resultados_muestras)
                for tipo in resultados_muestras[0]["errores"].keys()
            }

            self.resultados[nombre] = {
                "periodo": info['periodo'],
                "muestras_analizadas": len(resultados_muestras),
                "tasa_error_promedio": round(promedio_tasa_error, 2),
                "calidad_promedio": self.estimar_calidad(promedio_tasa_error),
                "errores_promedio": {k: round(v, 2) for k, v in promedio_errores.items()},
                "detalle_muestras": resultados_muestras
            }

            print(f"  ✓ Tasa de error promedio: {promedio_tasa_error:.2f}%")
            print(f"  ✓ Calidad estimada: {self.estimar_calidad(promedio_tasa_error)}")

    def analizar_todos(self):
        """Analiza todos los periódicos."""
        print("\n" + "="*80)
        print("ANÁLISIS DE CALIDAD OCR - PERIÓDICOS MADRILEÑOS (1849-1939)")
        print("Proyecto LexiMus USAL - PID2022-139589NB-C33")
        print("="*80)

        for nombre, info in PERIODICOS.items():
            self.analizar_periodico(nombre, info)

        self.generar_informe()

    def generar_informe(self):
        """Genera informe final con todos los resultados."""
        print("\n" + "="*80)
        print("RESUMEN GLOBAL")
        print("="*80)
        print(f"Total archivos analizados: {self.estadisticas_globales['total_archivos_analizados']}")
        print(f"Total líneas analizadas: {self.estadisticas_globales['total_lineas_analizadas']:,}")
        print(f"Total palabras analizadas: {self.estadisticas_globales['total_palabras_analizadas']:,}")

        # Calcular tasa de error global
        tasa_global = sum(r["tasa_error_promedio"] for r in self.resultados.values()) / len(self.resultados)
        print(f"\nTasa de error OCR global: {tasa_global:.2f}%")
        print(f"Calidad OCR global: {self.estimar_calidad(tasa_global)}")

        # Ranking de calidad
        print("\n" + "-"*80)
        print("RANKING DE CALIDAD POR PERIÓDICO:")
        print("-"*80)
        ranking = sorted(self.resultados.items(), key=lambda x: x[1]["tasa_error_promedio"])
        for i, (nombre, datos) in enumerate(ranking, 1):
            print(f"{i}. {nombre:30} | Tasa error: {datos['tasa_error_promedio']:6.2f}% | {datos['calidad_promedio']}")

        # Guardar resultados en JSON
        output_file = "/Users/maria/prensa-madrid-leximus/analisis_calidad_ocr.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump({
                "estadisticas_globales": self.estadisticas_globales,
                "tasa_error_global": round(tasa_global, 2),
                "calidad_global": self.estimar_calidad(tasa_global),
                "periodicos": self.resultados
            }, f, ensure_ascii=False, indent=2)

        print(f"\n✓ Resultados guardados en: {output_file}")

if __name__ == "__main__":
    analizador = AnalizadorCalidadOCR()
    analizador.analizar_todos()
