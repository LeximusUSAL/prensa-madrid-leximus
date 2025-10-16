# Análisis de la Música en la Prensa Diaria Madrileña (1849-1939)

[![Proyecto LexiMus](https://img.shields.io/badge/Proyecto-LexiMus-blue)](https://github.com/leximusal)
[![Universidad de Salamanca](https://img.shields.io/badge/USAL-Salamanca-red)](https://usal.es)
[![Financiación](https://img.shields.io/badge/PID2022--139589NB--C33-Ministerio%20CCII-green)](https://www.ciencia.gob.es/)

## 📰 Descripción del Proyecto

Este repositorio contiene el análisis cronológico y cuantitativo de **13 periódicos diarios generalistas** de Madrid publicados entre 1849 y 1939, con el objetivo de estudiar la **representatividad de la palabra "música"** en los medios de comunicación no especializados durante finales del siglo XIX y principios del XX.

### 🎯 Objetivos

Desde el proyecto **LexiMus USAL** (PID2022-139589NB-C33) buscamos:

- **Analizar la presencia del léxico musical** en la prensa diaria generalista madrileña
- **Cuantificar la cobertura mediática** de temas musicales en contextos no especializados
- **Identificar patrones temporales** de interés por la música en la prensa generalista
- **Comparar** la representatividad musical entre diferentes periódicos y épocas
- **Establecer un corpus de referencia** para estudios de musicología digital e historia cultural

A diferencia de nuestro análisis previo de **revistas musicales especializadas**, este proyecto se centra en la **prensa diaria generalista** para comprender cómo la música se reflejaba en los medios de comunicación de masas.

## 📊 Corpus de Periódicos

### Periódicos Analizados

| Periódico | Período de Publicación | Duración | Ejemplares Digitalizados |
|-----------|------------------------|----------|-------------------------|
| **La Época** | 01/04/1849 - 31/03/1936 | 87.0 años | **28,854** |
| **La Correspondencia de España** | 02/01/1860 - 27/06/1925 | 65.5 años | **23,302** |
| **El Imparcial** | 01/01/1867 - 30/05/1933 | 66.4 años | **23,008** |
| **El Liberal** | 15/07/1879 - 26/03/1939 | 59.7 años | **19,840** |
| **El Heraldo de Madrid** | 29/10/1890 - 26/03/1939 | 48.4 años | **15,583** |
| **La Acción** | 28/02/1916 - 21/05/1924 | 8.2 años | **2,755** |
| **El Sol** | 29/11/1917 - 27/03/1939 | 21.3 años | **5,972** |
| **La Libertad** | 21/12/1919 - 26/03/1939 | 19.3 años | **5,902** |
| **La Voz** | 01/07/1920 - 27/03/1939 | 18.7 años | **5,358** |
| **La Nación** | 19/10/1925 - 13/03/1936 | 10.4 años | **3,105** |
| **Ahora** | 16/12/1930 - 05/12/1938 | 8.0 años | **2,186** |
| **Crisol** | 04/04/1931 - 06/01/1932 | 0.8 años | **202** |
| **Luz** | 07/01/1932 - 07/09/1934 | 2.7 años | **827** |

### 📈 Estadísticas del Corpus

- **Total de periódicos**: 13
- **Arco cronológico completo**: 1849-1939 (90 años)
- **Ejemplares digitalizados totales**: **136,894** (13 periódicos, 100% del corpus)
- **Período de máxima coincidencia**: 1931-1932 (2 años, 10 periódicos activos simultáneamente)
- **Contexto histórico clave**: Segunda República Española (1931)

## 🔬 Metodología

### Fuente de Datos

Los archivos TXT fueron obtenidos de la **Biblioteca Nacional de España (BNE)** a través de su Hemeroteca Digital.

### ⚠️ Limitaciones Reconocidas

**Errores de OCR**: Los textos digitalizados por la BNE presentan errores de reconocimiento óptico de caracteres (OCR), especialmente en:
- Tipografías antiguas del siglo XIX
- Páginas deterioradas o mal conservadas
- Formatos de columnas complejos
- Caracteres especiales y acentuación

### ✅ Compensación por Volumen

A pesar de estas limitaciones, consideramos que el análisis es válido por:
- **Enorme volumen de datos** (136,894 ejemplares)
- **Análisis sistemático** de todo el corpus
- **Representatividad estadística significativa**
- **Patrones generales** que trascienden errores individuales

> **Nota**: Los resultados deberán ser **revisados y contrastados** cuando la Hemeroteca de la BNE mejore el OCR de sus fuentes digitalizadas.

## 🛠️ Scripts de Análisis

### Archivos Incluidos

#### 1. `analisis_cronologico_periodicos_madrid.py`
Script principal que realiza:
- Análisis de arcos cronológicos de cada periódico
- Identificación del período de máxima coincidencia temporal
- Cálculo de duraciones y solapamientos
- Conteo de ejemplares digitalizados
- Generación de estadísticas en formato JSON

**Uso:**
```bash
python3 analisis_cronologico_periodicos_madrid.py
```

**Salida:**
- `analisis_cronologico_periodicos_madrid.json`: Datos estructurados del análisis

#### 2. `cronologia_periodicos_madrid.html`
Interfaz web interactiva con visualización de:
- Líneas de tiempo de cada periódico
- Período de máxima coincidencia
- Análisis de coincidencias parciales
- Contexto histórico

**Uso:**
```bash
# Abrir directamente en navegador
open cronologia_periodicos_madrid.html
```

### Dependencias

```python
# Python 3.x
from datetime import datetime
from collections import defaultdict
import json
```

No requiere instalación de paquetes externos.

## 📁 Estructura del Repositorio

```
prensa-madrid-leximus/
├── README.md                                    # Este archivo
├── scripts/
│   └── analisis_cronologico_periodicos_madrid.py  # Script de análisis
├── resultados/
│   ├── analisis_cronologico_periodicos_madrid.json  # Datos JSON
│   └── cronologia_periodicos_madrid.html            # Visualización web
└── docs/
    └── metodologia.md                           # Documentación metodológica
```

## 🎯 Hallazgos Principales

### Período de Máxima Coincidencia

**1931-1932** (2 años)

Este es el período donde más periódicos estuvieron activos simultáneamente (**10 de 13 periódicos**), coincidiendo con:
- Proclamación de la Segunda República Española (14 abril 1931)
- Momento de máxima efervescencia periodística en Madrid
- Auge de nuevas publicaciones republicanas (Crisol, Ahora, Luz)

### Distribución Temporal

| Nivel de Coincidencia | Períodos |
|----------------------|----------|
| 10 periódicos | 1931-1932 (2 años) |
| 9 periódicos | 1920-1923, 1933-1934 (6 años) |
| 8 periódicos | 1924, 1926-1930, 1935 (7 años) |
| 7 periódicos | 1918-1919, 1925 (3 años) |
| 6 periódicos | 1916-1917, 1936-1938 (5 años) |
| 5 periódicos | 1891-1915 (25 años) |
| 4 periódicos | 1880-1890 (11 años) |
| 3 periódicos | 1867-1879 (13 años) |
| 2 periódicos | 1860-1866 (7 años) |
| 1 periódico | 1849-1859 (11 años) |

### Cese de Publicaciones

La **Guerra Civil Española (1936-1939)** marcó el cierre masivo de periódicos, con la mayoría cesando en **marzo de 1939**.

## 🔗 Proyecto LexiMus

### Contexto Académico

**LexiMus: Léxico y ontología de la música en español**
- **Código**: PID2022-139589NB-C33
- **Institución principal**: Universidad de Salamanca (USAL)
- **Instituciones colaboradoras**:
  - Instituto Complutense de Ciencias Musicales
  - Universidad de La Rioja
- **Financiación**: Ministerio de Ciencia, Competitividad e Innovación (España)

### Objetivos Generales del Proyecto

- Crear una **ontología del léxico musical** en español
- Analizar la **evolución histórica** del vocabulario musical
- Estudiar **sesgos de género** en el discurso musical
- Investigar la **diversidad cultural** en la música española
- Aplicar **técnicas de procesamiento de lenguaje natural** a corpus musicales

### Corpus Previos Analizados

1. **Revistas musicales especializadas** (1842-2024): 19 publicaciones, 25.8 millones de palabras
2. **Prensa diaria generalista** (1849-1939): 13 periódicos madrileños, 136,894 ejemplares [ESTE PROYECTO]

## 📖 Publicaciones y Resultados

### Informes Generados

- `FINAL_COMPREHENSIVE_SPANISH_MUSIC_MAGAZINES_REPORT.md`: Análisis completo de revistas especializadas
- `analisis_cronologico_periodicos_madrid.json`: Datos cronológicos de prensa diaria

### Próximos Pasos

1. **Análisis léxico**: Extracción y cuantificación del vocabulario musical
2. **Análisis de frecuencias**: Términos musicales más frecuentes por período
3. **Análisis de contexto**: Cómo se habla de música en prensa generalista vs. especializada
4. **Análisis comparativo**: Diferencias entre periódicos conservadores y progresistas
5. **Visualizaciones**: Gráficos de evolución temporal del léxico musical

## 👥 Equipo de Investigación

**Universidad de Salamanca - Departamento de Musicología**
- Equipo LexiMus USAL

**Contacto**: mpalacios@usal.es

## 📄 Licencia

Este proyecto está bajo licencia **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

Los datos de la Hemeroteca Digital de la BNE están sujetos a sus propias condiciones de uso.

## 🙏 Agradecimientos

- **Biblioteca Nacional de España (BNE)** por la digitalización y acceso a la Hemeroteca Digital
- **Ministerio de Ciencia, Competitividad e Innovación** por la financiación del proyecto LexiMus
- **Universidad de Salamanca** por el apoyo institucional

## 📚 Cómo Citar

```bibtex
@misc{leximus_prensa_madrid_2025,
  title={Análisis de la Música en la Prensa Diaria Madrileña (1849-1939)},
  author={Proyecto LexiMus USAL},
  year={2025},
  publisher={GitHub},
  howpublished={https://github.com/[usuario]/prensa-madrid-leximus},
  note={PID2022-139589NB-C33}
}
```

## 🔄 Versión

**v1.0.0** - Octubre 2025
- Análisis cronológico inicial
- Conteo de ejemplares digitalizados
- Identificación de períodos de coincidencia

---

**Proyecto LexiMus USAL** | PID2022-139589NB-C33 | Universidad de Salamanca
