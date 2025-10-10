# Metodología del Proyecto

## Análisis de la Música en la Prensa Diaria Madrileña (1849-1939)

### 1. Objetivos de la Investigación

Este proyecto forma parte de **LexiMus USAL** (PID2022-139589NB-C33) y tiene como objetivo principal analizar la **representatividad de la palabra "música"** y el léxico musical asociado en los medios de comunicación generalistas (prensa diaria no especializada) del Madrid de finales del siglo XIX y principios del XX.

#### Objetivos específicos:

1. **Cuantificar la presencia** del vocabulario musical en prensa generalista
2. **Comparar** con corpus previos de revistas musicales especializadas
3. **Identificar patrones temporales** de interés mediático por la música
4. **Analizar contextos** en los que se menciona la música en medios generalistas
5. **Establecer diferencias** entre prensa conservadora y progresista

### 2. Corpus de Trabajo

#### 2.1 Selección de Periódicos

Se han seleccionado **8 periódicos diarios generalistas** de Madrid por:

- **Relevancia histórica**: Periódicos de amplia difusión en su época
- **Diversidad ideológica**: Conservadores (La Época), liberales (El Imparcial, El Liberal), republicanos (Crisol)
- **Cobertura temporal**: Arco de 90 años (1849-1939)
- **Disponibilidad**: Digitalizados en la Hemeroteca Digital de la BNE

#### 2.2 Caracterización del Corpus

| Periódico | Ideología | Período | Ejemplares |
|-----------|-----------|---------|------------|
| La Época | Conservador | 1849-1936 | N/D |
| El Imparcial | Liberal | 1867-1933 | 23,008 |
| El Liberal | Liberal | 1879-1939 | N/D |
| El Heraldo de Madrid | Republicano | 1890-1939 | N/D |
| El Sol | Liberal | 1917-1939 | 5,972 |
| La Libertad | Republicano | 1919-1939 | N/D |
| La Nación | Conservador | 1925-1936 | 3,105 |
| Crisol | Republicano | 1931-1932 | 202 |

**Total contabilizado**: 32,287 ejemplares (4 periódicos con datos disponibles)

### 3. Fuente de Datos

#### 3.1 Biblioteca Nacional de España (BNE)

Los textos digitalizados provienen de la **Hemeroteca Digital de la BNE**:
- Formato: Archivos TXT generados por OCR
- Acceso: Descarga directa desde http://hemerotecadigital.bne.es/

#### 3.2 Limitaciones del OCR

**Problemática identificada**:

1. **Errores de reconocimiento** en:
   - Tipografías antiguas (siglo XIX)
   - Páginas deterioradas
   - Formatos de columnas complejos
   - Caracteres especiales (acentos, ñ, signos musicales)

2. **Tipos de errores comunes**:
   - Sustituciones: "música" → "musica", "müsica"
   - Omisiones: palabras incompletas
   - Inserciones: caracteres espurios
   - Segmentación: palabras juntas o separadas incorrectamente

**Ejemplo de errores**:
```
Original esperado: "El concierto de música sinfónica"
OCR real: "El coneierto de musica sinfonica"
```

#### 3.3 Estrategia de Compensación

A pesar de las limitaciones del OCR, consideramos que el análisis tiene **validez estadística** por:

1. **Volumen masivo de datos**: 32,287+ ejemplares digitalizados
2. **Análisis sistemático**: Procesamiento uniforme de todo el corpus
3. **Redundancia estadística**: Los errores se diluyen en el gran volumen
4. **Patrones generales**: Las tendencias macro trascienden errores individuales

**Fórmula de representatividad**:
```
Representatividad = (Datos correctos / Datos totales) × Volumen × Sistematicidad

Aunque perdamos un 10-20% de datos por errores OCR,
el volumen compensa con representatividad significativa.
```

### 4. Procesamiento de Datos

#### 4.1 Análisis Cronológico (Fase Actual)

**Script**: `scripts/analisis_cronologico_periodicos_madrid.py`

**Funcionalidades**:
- Cálculo de arcos cronológicos por periódico
- Identificación de períodos de coincidencia temporal
- Conteo de ejemplares digitalizados
- Generación de estadísticas en JSON

**Métricas calculadas**:
- Duración de cada periódico (en años)
- Período de máxima coincidencia (8 periódicos simultáneos: abril 1931 - enero 1932)
- Niveles de coincidencia parcial (7, 6, 5... periódicos)
- Total de ejemplares disponibles

#### 4.2 Análisis Léxico (Fase Futura)

**Planificación**:

1. **Extracción de vocabulario musical**:
   - Términos de referencia del proyecto LexiMus
   - Categorías: géneros, instrumentos, técnica, instituciones

2. **Análisis de frecuencias**:
   - Frecuencia absoluta y relativa por período
   - Comparación entre periódicos
   - Evolución temporal

3. **Análisis de contexto**:
   - Colocaciones (palabras que acompañan términos musicales)
   - Análisis de sentimiento
   - Temas asociados a música

4. **Comparación con corpus especializado**:
   - Revistas musicales vs. prensa generalista
   - Diferencias en uso del vocabulario

### 5. Herramientas y Tecnologías

#### 5.1 Software

- **Python 3.x**: Procesamiento de datos
- **Librerías estándar**: `datetime`, `json`, `collections`
- **Futuro**: NLP (Natural Language Processing)

#### 5.2 Visualización

- **HTML5/CSS3**: Interfaz web interactiva
- **JavaScript**: Interactividad y animaciones
- **Design System**: Colores corporativos LexiMus (#008a9b, #00a0b4, #006d7a)

### 6. Control de Calidad

#### 6.1 Validación de Datos

- Verificación manual de muestras aleatorias
- Contrastación con fuentes secundarias
- Revisión de outliers estadísticos

#### 6.2 Reproducibilidad

- Scripts documentados y versionados en GitHub
- Datos estructurados en JSON
- Metodología explícita en documentación

### 7. Limitaciones Reconocidas

1. **Errores de OCR** (ya mencionado)
2. **Cobertura parcial**: Solo 4 de 8 periódicos con conteo de ejemplares
3. **Sesgos de digitalización**: La BNE puede haber priorizado ciertos períodos
4. **Sesgo geográfico**: Solo Madrid (no representa toda España)
5. **Sesgo de clase**: Prensa accesible principalmente a clases medias-altas

### 8. Consideraciones Éticas

- **Datos públicos**: Todo el material proviene de dominio público (BNE)
- **Transparencia**: Limitaciones expuestas claramente
- **Revisabilidad**: Resultados provisionales hasta mejora del OCR
- **Cita apropiada**: Reconocimiento a la BNE como fuente

### 9. Próximos Pasos

1. **Análisis léxico completo** del vocabulario musical
2. **Comparación estadística** con corpus de revistas especializadas
3. **Análisis de género**: Presencia de compositoras, intérpretes femeninas
4. **Análisis de diversidad**: Referencias a músicas no europeas
5. **Visualizaciones avanzadas**: Gráficos de evolución temporal
6. **Publicaciones académicas**: Artículos en revistas especializadas

### 10. Referencias Metodológicas

- **Proyecto LexiMus**: PID2022-139589NB-C33
- **Hemeroteca Digital BNE**: http://hemerotecadigital.bne.es/
- **Corpus previo**: Análisis de 19 revistas musicales españolas (1842-2024)

---

**Documento elaborado**: Octubre 2025
**Versión**: 1.0
**Proyecto**: LexiMus USAL - Universidad de Salamanca
