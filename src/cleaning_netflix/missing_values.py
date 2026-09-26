"Module de gestion des valeurs manquantes"

import numpy as np
import pandas as pd


def clean_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Orchestre le nettoyage des valeurs manquantes en gérant 
    les décalages et en remplaçant les valeurs manquantes 
    par des valeurs par défaut.

    :param df: DataFrame contenant les données
    :return: DataFrame avec les valeurs manquantes nettoyées
    """
    df = fix_duration_rating_shift(df)
    df = fill_missing_categoricals(df)
    return df


def fill_missing_categoricals(df: pd.DataFrame) -> pd.DataFrame:
    """
    Impute les colonnes catégorielles textuelles plutôt que de supprimer 
    les lignes, car le reste des données (titre, description, etc.) reste 
    exploitable. Pour `director`, `cast`, `country` (MAR, taux 9-30%), l'absence 
    est en grande partie structurelle (ex: TV Show sans réalisateur unique 
    crédité) plutôt qu'une absences de données lors de la collecte — nuance non traitée 
    séparément ici par souci de simplicité (voir NOTES.md).
    Pour `rating` (7 lignes), l'absence est ponctuelle sans pattern détecté.

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
