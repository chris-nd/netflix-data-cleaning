"Module de test pour le pipeline de nettoyage"

import pandas as pd
import pytest

from src.cleaning_netflix.pipeline import clean_netflix


@pytest.fixture
def sample_df():
    """
    Fixture pour créer un DataFrame d'exemple.
    """

    return pd.DataFrame({
        "type": ["Movie", "TV Show", "Movie"],
        "director": ["Jane", None, "Louis"],
        "cast": ["A", "B", "Louis"],
        "country": ["France", "USA", "USA"],
        "date_added": ["January 1, 2020", None, " April 4, 2017"],
        "rating": ["PG-13", "TV-MA", "74 min"],   # ligne 2 : cas Louis C.K.
        "duration": ["90 min", "2 Seasons", None],
    })


def test_clean_netflix_applique_toutes_les_etapes(sample_df):
    """
    Vérifie que le pipeline applique toutes les étapes de nettoyage.

    :param sample_df: DataFrame d'exemple
    """
    result = clean_netflix(sample_df)

    assert "duration" not in result.columns
    assert result.loc[0, "duration_minutes"] == 90
    assert result.loc[1, "duration_seasons"] == 2
    assert result.loc[2, "duration_minutes"] == 74       # fix + split enchaînés
    assert result.loc[2, "rating"] == "Unknown"
    assert result.loc[1, "director"] == "Not Specified"
    assert result.loc[2, "year_added"] == 2017
    assert pd.isna(result.loc[1, "date_added"])           # NaT attendu
