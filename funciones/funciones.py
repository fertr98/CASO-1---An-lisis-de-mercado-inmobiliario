import numpy as np
import pandas as pd

# -----------------------------------------------------------
# Cálculo de la distancia de Haversine
# -----------------------------------------------------------


def haversine(lat1, lon1, lat2, lon2):
    """
    Calcula la distancia entre coordenadas geográficas en kilómetros.

    Admite valores individuales y arrays de NumPy mediante broadcasting.

    Parámetros
    ----------
    lat1, lon1 : array-like
        Latitud y longitud del primer punto.
    lat2, lon2 : array-like
        Latitud y longitud del segundo punto.

    Devuelve
    --------
    Distancia en kilómetros.
    """
    R = 6371.0

    # Convertir cada argumento a radianes por separado
    lat1 = np.radians(lat1)
    lon1 = np.radians(lon1)
    lat2 = np.radians(lat2)
    lon2 = np.radians(lon2)

    # Diferencias de coordenadas
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Fórmula de Haversine
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2

    # Evitar errores numéricos por redondeo
    a = np.clip(a, 0, 1)

    return 2 * R * np.arcsin(np.sqrt(a))


# -----------------------------------------------------------
# Cálculo de la puntuación de proximidad a puntos de interés
# -----------------------------------------------------------


def calculate_poi_score(listings_full, pois, tau_km=1.5):
    """
    Calcula una puntuación de proximidad a puntos de interés (0-100).

    Utiliza distancias Haversine, decaimiento exponencial y pesos
    configurables para cada punto de interés.

    Parámetros
    ----------
    listings_full : pd.DataFrame
        DataFrame de inmuebles con columnas latitude y longitude.

    pois : pd.DataFrame
        DataFrame de puntos de interés con columnas lat, lon y weight.
        Los pesos deben estar comprendidos entre 0 y 1.

    tau_km : float, default=2
        Distancia de decaimiento exponencial en kilómetros.
        Cuanto mayor sea, más lentamente disminuirá la proximidad.

    Devuelve
    --------
    pd.DataFrame
        Copia del DataFrame de inmuebles con la columna poi_score.
        Los inmuebles con coordenadas inválidas reciben NaN.
    """

    # 1. Validar tau_km
    if (
        isinstance(tau_km, (bool, np.bool_))
        or not isinstance(tau_km, (int, float, np.integer, np.floating))
        or not np.isfinite(tau_km)
        or tau_km <= 0
    ):
        raise ValueError("tau_km debe ser un número finito mayor que 0.")

    # 2. Validar los DataFrames
    if not isinstance(listings_full, pd.DataFrame):
        raise TypeError("listings_full debe ser un DataFrame de pandas.")

    if not isinstance(pois, pd.DataFrame):
        raise TypeError("pois debe ser un DataFrame de pandas.")

    required_listings = {"latitude", "longitude"}
    required_pois = {"lat", "lon", "weight"}

    missing_listings = required_listings - set(listings_full.columns)
    missing_pois = required_pois - set(pois.columns)

    if missing_listings:
        raise ValueError(
            f"Faltan columnas en listings_full: {sorted(missing_listings)}"
        )

    if missing_pois:
        raise ValueError(f"Faltan columnas en pois: {sorted(missing_pois)}")

    # Comprobar que hay puntos de interés
    if pois.empty:
        raise ValueError("pois debe contener al menos un punto de interés.")

    # 3. Convertir coordenadas y pesos a valores numéricos
    lat = pd.to_numeric(listings_full["latitude"], errors="coerce").to_numpy(
        dtype=float, na_value=np.nan
    )

    lon = pd.to_numeric(listings_full["longitude"], errors="coerce").to_numpy(
        dtype=float, na_value=np.nan
    )

    poi_lat = pd.to_numeric(pois["lat"], errors="coerce").to_numpy(
        dtype=float, na_value=np.nan
    )

    poi_lon = pd.to_numeric(pois["lon"], errors="coerce").to_numpy(
        dtype=float, na_value=np.nan
    )

    weights = pd.to_numeric(pois["weight"], errors="coerce").to_numpy(
        dtype=float, na_value=np.nan
    )

    # 4. Validar coordenadas de los POI
    valid_pois = (
        np.isfinite(poi_lat)
        & np.isfinite(poi_lon)
        & (np.abs(poi_lat) <= 90)
        & (np.abs(poi_lon) <= 180)
    )

    if not valid_pois.all():
        raise ValueError(
            "Hay coordenadas inválidas en pois. " "Revisa las columnas lat y lon."
        )

    # 5. Validar pesos
    valid_weights = np.isfinite(weights) & (weights >= 0) & (weights <= 1)

    if not valid_weights.all():
        raise ValueError("Los pesos deben ser numéricos, finitos y estar entre 0 y 1.")

    if weights.sum() <= 0:
        raise ValueError("La suma de los pesos debe ser mayor que 0.")

    # 6. Identificar inmuebles con coordenadas válidas
    valid = (
        np.isfinite(lat) & np.isfinite(lon) & (np.abs(lat) <= 90) & (np.abs(lon) <= 180)
    )

    # 7. Inicializar puntuaciones
    poi_score = np.full(len(listings_full), np.nan)

    # 8. Calcular distancias y puntuaciones
    # Solo se procesan los inmuebles con coordenadas válidas
    if valid.any():

        distances = haversine(
            lat[valid, None], lon[valid, None], poi_lat[None, :], poi_lon[None, :]
        )

        # Decaimiento exponencial de la proximidad
        proximity = np.exp(-distances / tau_km)

        # Media ponderada normalizada entre 0 y 100
        poi_score[valid] = 100 * (proximity @ weights) / weights.sum()

    # 9. Añadir la variable al DataFrame sin modificar el original
    result = listings_full.copy()
    result["poi_score"] = poi_score

    return result


# ---------------------------------------------------------
# Creación mapa de calor de Madrid en función del poi_score
# ----------------------------------------------------------


def create_poi_heatmap(
    listings_full,
    zoom_start=11,
    radius=18,
    blur=15,
    min_opacity=0.25,
):
    """
    Crea un mapa de calor ponderado por poi_score a partir de las coordenadas
    de los inmuebles.

    Parámetros
    ----------
    listings_full : pd.DataFrame
        DataFrame con las columnas latitude, longitude y poi_score.
    zoom_start : int, default=11
        Nivel de zoom inicial del mapa.
    radius : int, default=18
        Radio de influencia de cada punto en el mapa de calor.
    blur : int, default=15
        Desenfoque aplicado a los puntos.
    min_opacity : float, default=0.25
        Opacidad mínima del mapa de calor.

    Devuelve
    --------
    folium.Map
        Mapa de calor centrado en las coordenadas medias de los inmuebles.
    """
    if not isinstance(listings_full, pd.DataFrame):
        raise TypeError("listings_full debe ser un DataFrame de pandas.")

    required_columns = {"latitude", "longitude", "poi_score"}
    missing_columns = required_columns - set(listings_full.columns)
    if missing_columns:
        raise ValueError(f"Faltan columnas en listings_full: {sorted(missing_columns)}")

    # Importación local para no requerir Folium al importar el módulo completo.
    import folium
    from folium.plugins import HeatMap

    mapa_datos = listings_full[["latitude", "longitude", "poi_score"]].copy()
    for column in ["latitude", "longitude", "poi_score"]:
        mapa_datos[column] = pd.to_numeric(mapa_datos[column], errors="coerce")

    mapa_datos = mapa_datos.dropna()
    mapa_datos = mapa_datos[
        mapa_datos["latitude"].between(-90, 90)
        & mapa_datos["longitude"].between(-180, 180)
    ]

    if mapa_datos.empty:
        raise ValueError(
            "No hay filas con latitude, longitude y poi_score válidos para crear el mapa."
        )

    min_score = mapa_datos["poi_score"].min()
    max_score = mapa_datos["poi_score"].max()

    if max_score == min_score:
        mapa_datos["intensidad"] = 1.0
    else:
        mapa_datos["intensidad"] = (mapa_datos["poi_score"] - min_score) / (
            max_score - min_score
        )

    centro_madrid = [
        mapa_datos["latitude"].mean(),
        mapa_datos["longitude"].mean(),
    ]

    mapa_poi = folium.Map(
        location=centro_madrid,
        zoom_start=zoom_start,
        tiles="OpenStreetMap",
    )

    HeatMap(
        mapa_datos[["latitude", "longitude", "intensidad"]].values.tolist(),
        gradient={
            0.0: "blue",
            0.5: "yellow",
            1.0: "red",
        },
        radius=radius,
        blur=blur,
        min_opacity=min_opacity,
    ).add_to(mapa_poi)

    return mapa_poi
