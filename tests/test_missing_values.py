"""Module de test pour les fonctions de nettoyage des valeurs manquantes"""

import pandas as pd
import pytest

from src.cleaning_netflix.missing_values import (
    clean_missing_values,
    fill_missing_categoricals,
    fix_duration_rating_shift,
)


@pytest.fixture(name="sample_df")
def sample_data() -> pd.DataFrame:
    """DataFrame synthétique couvrant les cas rencontrés dans l'analyse :
    valeurs manquantes normales + le cas de décalage type Louis C.K.
    (rating contient une durée, duration est vide)."""
    return pd.DataFrame({
        "director": ["Jane Doe", None, "John Smith"],
        "cast": ["A, B", None, "C, D"],
        "country": ["France", None, "USA"],
        "rating": ["PG-13", "TV-MA", "74 min"],   # ligne 2 = cas Louis C.K.
        "duration": ["90 min", "2 Seasons", None], # ligne 2 = duration vide
    })


def test_fill_missing_categoricals_impute_les_bonnes_valeurs(sample_df):
    """
    Vérifie que chaque colonne catégorielle est remplie avec la bonne valeur par défaut.

    :param sample_df: DataFrame de test
    """

    result = fill_missing_categoricals(sample_df)

    assert result.loc[1, "director"] == "Not Specified"
    assert result.loc[1, "cast"] == "Not Specified"
    assert result.loc[1, "country"] == "Not Specified"
    assert result[["director", "cast", "country", "rating"]].isnull().sum().sum() == 0


def test_fill_missing_categoricals_ne_modifie_pas_l_original(sample_df):
    """
    Garantit l'absence d'effet de bord sur le DataFrame passé en paramètre.

    :param sample_df: DataFrame de test
    """

    original = sample_df.copy()
    _ = fill_missing_categoricals(sample_df)
    pd.testing.assert_frame_equal(sample_df, original)


def test_fix_duration_rating_shift_recupere_la_bonne_valeur(sample_df):
    """
    Vérifie que la valeur mal placée dans rating est bien déplacée vers duration.

    :param sample_df: DataFrame de test
    """

    result = fix_duration_rating_shift(sample_df)

    assert result.loc[2, "duration"] == "74 min"
    assert pd.isna(result.loc[2, "rating"])
    # les lignes non concernées par le bug ne doivent pas être touchées
    assert result.loc[0, "duration"] == "90 min"
    assert result.loc[0, "rating"] == "PG-13"


def test_fix_duration_rating_shift_ne_modifie_pas_l_original(sample_df):
    """
    Garantit l'absence d'effet de bord sur le DataFrame passé en paramètre.

    :param sample_df: DataFrame de test
    """

    original = sample_df.copy()
    _ = fix_duration_rating_shift(sample_df)
    pd.testing.assert_frame_equal(sample_df, original)


def test_clean_missing_values_orchestre_dans_le_bon_ordre(sample_df):
    """
    Vérifie que l'orchestrateur applique bien les deux corrections,
    et que le cas Louis C.K. (rating='74 min') finit avec duration='74 min'
    et rating='Unknown' (pas 'Not Specified', car rating a sa propre valeur).

    :param sample_df: DataFrame de test
    """

    result = clean_missing_values(sample_df)

    assert result.isnull().sum().sum() == 0
    assert result.loc[2, "duration"] == "74 min"
    assert result.loc[2, "rating"] == "Unknown"
