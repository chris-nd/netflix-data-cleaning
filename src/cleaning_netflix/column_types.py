"Module de nettoyage des colonnes de types mixtes"

import numpy as np
import pandas as pd


def split_duration(df: pd.DataFrame) -> pd.DataFrame:
    """
    Sépare `duration` (texte mixte "90 min" / "3 Seasons") en deux
    colonnes numériques distinctes selon le principe tidy data :
    minutes et saisons ne sont pas la même variable, donc pas la même colonne.
    NaN structurel attendu : duration_minutes est NaN pour un TV Show,
    duration_seasons est NaN pour un Movie.

    :param df: DataFrame avec la colonne 'duration' à séparer
    :return: DataFrame avec les colonnes 'duration_minutes' et 'duration_seasons'
    """

    df = df.copy()

    mask_movie = df["type"] == "Movie"

    df["duration_minutes"] = np.nan
    df["duration_seasons"] = np.nan

    df.loc[mask_movie, "duration_minutes"] = pd.to_numeric(
        df.loc[mask_movie, "duration"].str.extract(r"(\d+)")[0], errors="coerce"
    )

    df.loc[~mask_movie, "duration_seasons"] = pd.to_numeric(
        df.loc[~mask_movie, "duration"].str.extract(r"(\d+)")[0], errors="coerce"
    )

    return df.drop(columns="duration")
