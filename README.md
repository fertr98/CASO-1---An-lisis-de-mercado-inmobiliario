 informe final web entregable: file:///C:/Users/fishm/Desktop/ds4b_master/BLOQUE%20II%20BUSINESS%20ANALYTICS/000_casos%20business%20analytics/CASO%201%20-%20An%C3%A1lisis%20de%20mercado%20inmobiliario/entregables/informes/informe_ejecutivo_mercado_inmobiliario_madrid.html

# Análisis del mercado inmobiliario turístico de Madrid
### Business Analytics · Exploratory Data Analysis · Geospatial Analysis

Análisis de mercado orientado a identificar oportunidades de inversión en el sector del alquiler turístico en Madrid, mediante el estudio de precios, ocupación estimada, tipología de alojamiento, competencia y márgenes brutos.

El proyecto combina análisis exploratorio de datos (EDA), segmentación de mercado y visualización geoespacial para transformar datos de anuncios inmobiliarios en información útil para la toma de decisiones empresariales.

---

## 1. Objetivo del proyecto

El objetivo es analizar la estructura del mercado de alquiler turístico en Madrid para identificar qué características de los inmuebles y qué segmentos geográficos presentan un mayor potencial económico.

El análisis busca responder a cinco cuestiones principales:

- **Localización:** ¿Qué distritos presentan los precios medios por noche más elevados?
- **Tipología:** ¿Qué tipo de alojamiento ofrece mejores indicadores económicos?
- **Ocupación:** ¿Qué zonas presentan una mayor demanda estimada?
- **Competencia:** ¿Cómo se distribuye la oferta y qué diferencias existen entre segmentos?
- **Rentabilidad:** ¿Qué combinación de características puede resultar más interesante desde una perspectiva de inversión?

## 2. Dataset

El análisis parte de una muestra de **11.771 anuncios de alojamientos turísticos en Madrid**.

Se trabaja con información relativa a las características de los inmuebles, su localización geográfica y diferentes indicadores económicos y operativos.

Entre las variables de interés se encuentran:

| Dimensión | Variables analizadas |
|---|---|
| Localización | Distrito, barrio, latitud y longitud |
| Alojamiento | Tipo de propiedad, capacidad y dormitorios |
| Precio | Precio medio por noche |
| Demanda | Días de ocupación estimada |
| Competencia | Número y distribución de anuncios |
| Indicadores económicos | Margen bruto estimado |

## 3. Metodología

El proyecto sigue un flujo de trabajo orientado al análisis de negocio:

**01. Exploratory Data Analysis (EDA)**

- Exploración de la estructura y calidad del conjunto de datos.
- Análisis de distribuciones y estadísticas descriptivas.
- Identificación de valores atípicos y patrones relevantes.
- Análisis de variables geográficas, económicas y operativas.

**02. Segmentación del mercado**

- Comparación de precios entre distritos y barrios.
- Análisis por tipología de alojamiento.
- Evaluación de la ocupación estimada.
- Comparación de márgenes brutos entre segmentos.
- Estudio de la concentración de la oferta.

**03. Análisis geoespacial**

Se desarrolla una visualización interactiva mediante **Folium** para representar geográficamente los anuncios y analizar su distribución espacial.

El mapa incorpora marcadores geolocalizados y una codificación visual basada en el margen bruto estimado, facilitando la identificación de patrones territoriales y posibles concentraciones de oportunidades.

**04. Interpretación de resultados**

Los resultados se traducen en conclusiones orientadas a negocio, priorizando la identificación de segmentos atractivos frente a una interpretación exclusivamente descriptiva de los datos.

**05. Comunicación ejecutiva**

Se desarrolla un informe ejecutivo en HTML que sintetiza los principales hallazgos, presenta evidencias cuantitativas y formula recomendaciones estratégicas siguiendo una estructura de comunicación piramidal: conclusión, argumentos y evidencias.

## 4. Principales resultados

El análisis identifica diferencias relevantes entre las tipologías de alojamiento y los segmentos geográficos.

### 4.1. La tipología del inmueble es un factor diferencial

| Tipo de alojamiento | Precio medio/noche | Margen bruto medio |
|---|---:|---:|
| Vivienda completa | 211,76 € | 9,61 % |
| Habitación privada | 94,44 € | 4,43 % |
| Habitación compartida | 31,37 € | 1,15 % |

Las viviendas completas presentan los indicadores económicos más elevados de la muestra, tanto en precio medio por noche como en margen bruto.

### 4.2. La localización influye en el posicionamiento de precios

Algunos de los distritos con mayores precios medios por noche son:

| Distrito | Precio medio/noche |
|---|---:|
| Salamanca | 241,70 € |
| Centro | 210,85 € |
| Chamberí | 189,66 € |
| Retiro | 184,52 € |
| Chamartín | 184,01 € |

Sin embargo, un precio superior no implica necesariamente una mayor rentabilidad. Es necesario considerar conjuntamente la ocupación, el coste de adquisición y los gastos asociados.

### 4.3. La ocupación introduce una dimensión operativa

Entre los distritos destacados por ocupación estimada se encuentran:

- Barajas: 192 días.
- Villa de Vallecas: 168 días.
- Centro: 156 días.
- Arganzuela: 156 días.

Esto pone de manifiesto la importancia de combinar el potencial de ingresos por noche con la capacidad de generar demanda recurrente.

### 4.4. El margen depende de la combinación de variables

La segmentación por distrito y tipología permite identificar diferencias en los márgenes brutos observados.

Salamanca, Latina y Centro destacan en la comparación de viviendas completas incluida en el informe, aunque estos resultados deben contrastarse con los costes reales de adquisición y explotación.

## 5. Conclusiones estratégicas

A partir de los resultados obtenidos, se plantean las siguientes líneas de actuación:

1. **Priorizar viviendas completas:** presentan los mejores indicadores de precio y margen bruto dentro de la muestra.
2. **Analizar activos de capacidad media-alta:** estudiar especialmente viviendas de 2 a 4 dormitorios y capacidad para 4-5 o más huéspedes.
3. **Evaluar zonas por rendimiento potencial:** evitar seleccionar ubicaciones exclusivamente por sus precios medios.
4. **Incorporar la presión competitiva:** analizar la concentración de anuncios y las diferencias entre barrios.
5. **Validar la rentabilidad real:** incorporar costes de adquisición, financiación, mantenimiento, impuestos, gestión y requisitos regulatorios.

La principal conclusión es que el potencial de inversión no depende únicamente de la ubicación, sino de la combinación entre características del inmueble, capacidad de generar ingresos y estructura de costes.

---

## 6. Tecnologías y herramientas

| Tecnología | Aplicación |
|---|---|
| Python | Desarrollo del análisis |
| Pandas | Manipulación y análisis de datos |
| Jupyter Notebook | Desarrollo y documentación del análisis |
| Folium | Visualización geoespacial interactiva |
| HTML / CSS | Desarrollo del informe ejecutivo |
| VS Code | Entorno de desarrollo |

## 7. Entregables

El proyecto genera dos entregables principales:

**1. Mapa interactivo de oportunidades**

Visualización geográfica de los anuncios de Madrid, con marcadores representados mediante una escala visual asociada al margen bruto estimado.

Archivo: `mapa_margen.html`

**2. Informe ejecutivo de mercado**

Documento HTML con los principales indicadores, comparativas, conclusiones y recomendaciones de inversión.

Archivo: `informe_ejecutivo_mercado_inmobiliario_madrid.html`

## 8. Limitaciones del análisis

Los resultados deben interpretarse teniendo en cuenta las siguientes limitaciones:

- La ocupación utilizada es estimada y no equivale necesariamente a ocupación real.
- El margen bruto no representa la rentabilidad neta del inversor.
- No se incorpora un modelo completo de costes de adquisición y explotación.
- No se evalúa de forma exhaustiva la estacionalidad de la demanda.
- La viabilidad de cada operación depende también de la normativa aplicable y de los requisitos legales del alquiler turístico.

Por tanto, los resultados permiten identificar segmentos interesantes para profundizar en su análisis, pero no constituyen una recomendación de inversión individualizada.

---

## 9. Estructura del proyecto

```text
CASO 1 - Análisis de mercado inmobiliario/
│
├── .git
├── .github/
│   └── copilot-instructions.md
├── .gitignore
│
├── datos/
│   ├── brutos/
│   │   ├── euros_m2_madrid.csv
│   │   └── pois.csv
│   │
│   ├── intermedios/
│   │   └── inmobiliario.sqlite
│   │
│   └── procesados/
│       ├── listings_con_price_m2.csv
│       └── listings_det.csv
│
├── docs/
│   ├── metodologia_minicubos.md
│   ├── mapa_madrid_poi_score.html
│   ├── mapa_margen.html
│   └── proyecto-objetivos.md
│
├── entregables/
│   └── informes/
│       └── informe_ejecutivo_mercado_inmobiliario_madrid.html
│
├── funciones/
│   ├── __pycache__/
│   │   ├── funciones.cpython-311.pyc
│   │   └── funciones.cpython-313.pyc
│   └── funciones.py
│
├── notebooks/
│   ├── 01_importaciondatos.ipynb
│   ├── 02_creaciónvariables.ipynb
│   └── 03_analisis.ipynb
```
---

## Autor

Proyecto desarrollado como caso práctico de **Business Analytics**, aplicando técnicas de análisis de datos, segmentación de mercado y visualización para resolver un problema de negocio.

**Fernando Tejada**

[GitHub](https://github.com/) · [LinkedIn](https://www.linkedin.com/)
