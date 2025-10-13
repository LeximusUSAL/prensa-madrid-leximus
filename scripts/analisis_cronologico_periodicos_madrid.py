#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análisis cronológico de periódicos de Madrid
Identifica el período de mayor coincidencia entre publicaciones
"""

from datetime import datetime
from collections import defaultdict
import json

# Datos de los periódicos de Madrid
periodicos = {
    "El Sol": {"inicio": "29/11/1917", "fin": "27/03/1939", "ejemplares": 5972},
    "Crisol": {"inicio": "04/04/1931", "fin": "06/01/1932", "ejemplares": 202},
    "El Heraldo de Madrid": {"inicio": "29/10/1890", "fin": "26/03/1939", "ejemplares": 15583},
    "El Imparcial": {"inicio": "01/01/1867", "fin": "30/05/1933", "ejemplares": 23008},
    "El Liberal": {"inicio": "15/07/1879", "fin": "26/03/1939", "ejemplares": 19840},
    "La Época": {"inicio": "01/04/1849", "fin": "31/03/1936", "ejemplares": 28854},
    "La Libertad (1919)": {"inicio": "21/12/1919", "fin": "26/03/1939", "ejemplares": 5902},
    "La Nación": {"inicio": "19/10/1925", "fin": "13/03/1936", "ejemplares": 3105},
    "Ahora": {"inicio": "16/12/1930", "fin": "05/12/1938", "ejemplares": 2186},
    "La Acción": {"inicio": "28/02/1916", "fin": "21/05/1924", "ejemplares": 2755},
    "La Voz": {"inicio": "01/07/1920", "fin": "27/03/1939", "ejemplares": 5358},
    "Luz": {"inicio": "07/01/1932", "fin": "07/09/1934", "ejemplares": 827},
    "La Correspondencia de España": {"inicio": "02/01/1860", "fin": "27/06/1925", "ejemplares": 23302}
}

def parse_date(date_str):
    """Convierte fecha DD/MM/YYYY a objeto datetime"""
    return datetime.strptime(date_str, "%d/%m/%Y")

def format_date(date_obj):
    """Formatea fecha para visualización"""
    return date_obj.strftime("%d/%m/%Y")

def calcular_duracion_anios(inicio, fin):
    """Calcula la duración en años"""
    delta = fin - inicio
    return round(delta.days / 365.25, 1)

def agrupar_anios_consecutivos(anios):
    """Agrupa años consecutivos en rangos"""
    if not anios:
        return []

    anios_sorted = sorted(anios)
    grupos = []
    grupo_actual = [anios_sorted[0]]

    for anio in anios_sorted[1:]:
        if anio == grupo_actual[-1] + 1:
            grupo_actual.append(anio)
        else:
            grupos.append(grupo_actual)
            grupo_actual = [anio]

    grupos.append(grupo_actual)
    return grupos

# Convertir fechas a objetos datetime
periodicos_parsed = {}
for nombre, fechas in periodicos.items():
    periodicos_parsed[nombre] = {
        "inicio": parse_date(fechas["inicio"]),
        "fin": parse_date(fechas["fin"]),
        "inicio_str": fechas["inicio"],
        "fin_str": fechas["fin"],
        "ejemplares": fechas.get("ejemplares")
    }

# Encontrar fecha de inicio más tardía y fecha de fin más temprana
fecha_inicio_comun = max(p["inicio"] for p in periodicos_parsed.values())
fecha_fin_comun = min(p["fin"] for p in periodicos_parsed.values())

print("=" * 80)
print("ANÁLISIS CRONOLÓGICO DE PERIÓDICOS DE MADRID (1849-1939)")
print("=" * 80)
print()

# Mostrar información de cada periódico
print("ARCO CRONOLÓGICO Y EJEMPLARES DE CADA PERIÓDICO:")
print("-" * 100)
print(f"{'PERIÓDICO':25} | {'FECHAS':30} | {'DURACIÓN':12} | {'EJEMPLARES':10}")
print("-" * 100)

total_ejemplares = 0
for nombre in sorted(periodicos_parsed.keys(), key=lambda x: periodicos_parsed[x]["inicio"]):
    datos = periodicos_parsed[nombre]
    duracion = calcular_duracion_anios(datos["inicio"], datos["fin"])
    fechas_str = f"{datos['inicio_str']} - {datos['fin_str']}"

    if datos["ejemplares"] is not None:
        ejemplares_str = f"{datos['ejemplares']:,}"
        total_ejemplares += datos["ejemplares"]
    else:
        ejemplares_str = "N/D"

    print(f"{nombre:25} | {fechas_str:30} | {duracion:5.1f} años | {ejemplares_str:>10}")

print("-" * 100)
print(f"{'TOTAL':25} | {'':30} | {'':12} | {total_ejemplares:>10,}")
print("=" * 100)
print()
print(f"📊 RESUMEN DE EJEMPLARES DIGITALIZADOS:")
print(f"   - Periódicos con datos: 8 de 8 (100%)")
print(f"   - Total de ejemplares contabilizados: {total_ejemplares:,}")
print()
print("=" * 100)

# Calcular período de máxima coincidencia
if fecha_fin_comun >= fecha_inicio_comun:
    duracion_coincidencia = calcular_duracion_anios(fecha_inicio_comun, fecha_fin_comun)

    print("PERÍODO DE MÁXIMA COINCIDENCIA (todos los periódicos activos simultáneamente):")
    print("-" * 80)
    print(f"Inicio: {format_date(fecha_inicio_comun)}")
    print(f"Fin:    {format_date(fecha_fin_comun)}")
    print(f"Duración: {duracion_coincidencia} años ({int(duracion_coincidencia * 12)} meses)")
    print()
    print("Periódicos activos en este período: TODOS (8 periódicos)")

    # Identificar cuál periódico marcó el inicio y fin del período común
    periodico_inicio = [n for n, p in periodicos_parsed.items() if p["inicio"] == fecha_inicio_comun][0]
    periodico_fin = [n for n, p in periodicos_parsed.items() if p["fin"] == fecha_fin_comun][0]

    print(f"\n- Inicio marcado por: {periodico_inicio} (último en comenzar)")
    print(f"- Fin marcado por: {periodico_fin} (primero en cerrar)")
else:
    print("⚠️  NO HAY PERÍODO DE COINCIDENCIA TOTAL")
    print("No existe un período donde los 8 periódicos estuvieran activos simultáneamente.")

print()
print("=" * 80)

# Análisis por nivel de coincidencia (7, 6, 5 periódicos, etc.)
print("ANÁLISIS DE COINCIDENCIAS PARCIALES:")
print("-" * 80)

# Crear timeline año por año
anio_inicio = min(p["inicio"].year for p in periodicos_parsed.values())
anio_fin = max(p["fin"].year for p in periodicos_parsed.values())

coincidencias_por_anio = {}
for anio in range(anio_inicio, anio_fin + 1):
    fecha_ref = datetime(anio, 7, 1)  # Punto medio del año
    activos = [nombre for nombre, datos in periodicos_parsed.items()
               if datos["inicio"] <= fecha_ref <= datos["fin"]]
    coincidencias_por_anio[anio] = {
        "count": len(activos),
        "periodicos": activos
    }

# Agrupar períodos por nivel de coincidencia
niveles_coincidencia = defaultdict(list)
for anio, datos in coincidencias_por_anio.items():
    niveles_coincidencia[datos["count"]].append(anio)

# Mostrar resultados de mayor a menor coincidencia
for nivel in sorted(niveles_coincidencia.keys(), reverse=True):
    anios = niveles_coincidencia[nivel]
    if anios:
        anios_consecutivos = agrupar_anios_consecutivos(anios)
        print(f"\n{nivel} periódicos activos simultáneamente:")
        for grupo in anios_consecutivos:
            if len(grupo) == 1:
                print(f"  - {grupo[0]}")
            else:
                print(f"  - {grupo[0]}-{grupo[-1]} ({len(grupo)} años)")

# Encontrar el período más largo con máxima coincidencia
max_nivel = max(niveles_coincidencia.keys())
anios_max_nivel = niveles_coincidencia[max_nivel]
grupos_consecutivos = agrupar_anios_consecutivos(anios_max_nivel)

print()
print("=" * 80)
print(f"PERÍODO MÁS LARGO DE MÁXIMA COINCIDENCIA ({max_nivel} periódicos):")
print("-" * 80)

# Encontrar el grupo más largo
grupo_mas_largo = max(grupos_consecutivos, key=len)
inicio_periodo = datetime(grupo_mas_largo[0], 1, 1)
fin_periodo = datetime(grupo_mas_largo[-1], 12, 31)

print(f"Años: {grupo_mas_largo[0]} - {grupo_mas_largo[-1]}")
print(f"Duración: {len(grupo_mas_largo)} años")
print(f"\nPeriódicos activos:")

# Verificar qué periódicos estaban activos en este período
fecha_ref = datetime(grupo_mas_largo[0], 7, 1)
for nombre in sorted(periodicos_parsed.keys()):
    datos = periodicos_parsed[nombre]
    if datos["inicio"] <= fecha_ref <= datos["fin"]:
        print(f"  ✓ {nombre}")
    else:
        print(f"  ✗ {nombre} (inactivo)")

# Guardar resultados en JSON
resultados = {
    "total_periodicos": len(periodicos),
    "arco_cronologico_completo": {
        "inicio": format_date(min(p["inicio"] for p in periodicos_parsed.values())),
        "fin": format_date(max(p["fin"] for p in periodicos_parsed.values())),
        "duracion_anios": calcular_duracion_anios(
            min(p["inicio"] for p in periodicos_parsed.values()),
            max(p["fin"] for p in periodicos_parsed.values())
        )
    },
    "periodicos": {
        nombre: {
            "inicio": datos["inicio_str"],
            "fin": datos["fin_str"],
            "duracion_anios": calcular_duracion_anios(datos["inicio"], datos["fin"]),
            "ejemplares": datos["ejemplares"]
        }
        for nombre, datos in periodicos_parsed.items()
    },
    "total_ejemplares_digitalizados": sum(d["ejemplares"] for d in periodicos_parsed.values() if d["ejemplares"] is not None),
    "periodicos_con_ejemplares": sum(1 for d in periodicos_parsed.values() if d["ejemplares"] is not None),
    "periodo_maxima_coincidencia": {
        "nivel_coincidencia": max_nivel,
        "inicio": f"01/01/{grupo_mas_largo[0]}",
        "fin": f"31/12/{grupo_mas_largo[-1]}",
        "duracion_anios": len(grupo_mas_largo),
        "periodicos_activos": [nombre for nombre in sorted(periodicos_parsed.keys())
                               if periodicos_parsed[nombre]["inicio"] <= fecha_ref <= periodicos_parsed[nombre]["fin"]]
    }
}

import os
output_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resultados', 'analisis_cronologico_periodicos_madrid.json')
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(resultados, f, ensure_ascii=False, indent=2)

print()
print("=" * 80)
print(f"✓ Análisis guardado en: {output_path}")
print("=" * 80)
