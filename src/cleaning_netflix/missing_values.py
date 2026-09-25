"Module de gestion des valeurs manquantes"

import numpy as np
import pandas as pd


def fill_missing_categoricals(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remplit les valeurs manquantes dans les colonnes catégoriques.

    :param df: DataFrame contenant les données
    :return: DataFrame avec les valeurs manquantes remplies
    """
    df = df.copy()
    df['director'] = df['director'].fillna('Not Specified')
    df['cast'] = df['cast'].fillna('Not Specified')
    df['country'] = df['country'].fillna('Not Specified')
    df['rating'] = df['rating'].fillna("Unknown")
    return df


def fix_duration_rating_shift(df: pd.DataFrame) -> pd.DataFrame:
    """
    Corrige le décalage entre les colonnes duration et rating.

    :param df: DataFrame contenant les données
    :return: DataFrame avec les valeurs corrigées
    """
    df = df.copy()
    mask = df['duration'].isna()
    df.loc[mask, 'duration'] = df.loc[mask, 'rating']
    df.loc[mask, 'rating'] = np.nan
    return df
