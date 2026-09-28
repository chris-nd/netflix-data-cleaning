"""Module de test pour les types mixtes"""

import pandas as pd
import pytest

from cleaning_netflix.column_types import split_duration


# Fixture synthétique
@pytest.fixture(name="sample_df")
def sample_data() -> pd.DataFrame:
    """
    DataFrame synthétique ciblant split_duration : un Movie normal,
    un TV Show normal, et un Movie avec duration manquante (cas limite).
    """

    return pd.DataFrame(
        {
            "type": ["Movie", "TV Show", "Movie"],
            "duration": ["90 min", "2 Seasons", None],
        }
    )


def test_split_duration_extrait_les_bonnes_valeurs(sample_df):
    """
    Vérifie l'extraction numérique et les NaN structurels attendus.

    :param sample_df: DataFrame de test
    """
    result = split_duration(sample_df)

    assert "duration" not in result.columns

    assert result.loc[0, "duration_minutes"] == 90
    assert pd.isna(result.loc[0, "duration_seasons"])

    assert result.loc[1, "duration_seasons"] == 2
    assert pd.isna(result.loc[1, "duration_minutes"])

    # cas limite : duration déjà NaN en entrée -> les deux colonnes restent NaN
    assert pd.isna(result.loc[2, "duration_minutes"])
    assert pd.isna(result.loc[2, "duration_seasons"])


def test_split_duration_ne_modifie_pas_l_original(sample_df):
    """
    Garantit l'absence d'effet de bord sur le DataFrame passé en paramètre.

    :param sample_df: DataFrame de test
    """

    original = sample_df.copy()
    _ = split_duration(sample_df)

    # Vérifier que deux DataFrame sont égaux
    pd.testing.assert_frame_equal(sample_df, original)
