"Module de test pour la gestion des dates"

import numpy as np
import pandas as pd
import pytest

from src.cleaning_netflix.dates import parse_date_added


@pytest.fixture(name="sample_df")
def sample_data():
    """
    Fixture pour créer un DataFrame d'exemple.
    """

    return pd.DataFrame({
        "date_added": ["January 1, 2020", " February 1, 2020", None]
    })


def test_parse_data_added(sample_df):
    """
    Vérifie que la fonction parse_date_added fonctionne correctement.

    :param sample_df: DataFrame d'exemple.
    """

    result = parse_date_added(sample_df)

    assert result.loc[0, "month_added"] == 1
    assert result.loc[0, "year_added"] == 2020

    assert result.loc[1, "month_added"] == 2
    assert result.loc[1, "year_added"] == 2020

    assert pd.isna(result.loc[2, "month_added"])
    assert pd.isna(result.loc[2, "year_added"])


@pytest.mark.parametrize(
        "date", [
            "2021-09-25", 
            "09/25/2021", 
            "25/09/2021", 
            "Sat, 25 Sep 21"
        ]
)
def test_format_inattendu_leve_une_erreur(date):
    """
    Vérifie que les formats inattendus levent une erreur.

    :param date: Date au format inattendu.
    """

    df = pd.DataFrame({"date_added": [date]})
    with pytest.raises(ValueError):
        parse_date_added(df)


def test_date_type(sample_df):
    """
    Vérifie que les dates sont du bon type.

    :param sample_df: DataFrame d'exemple.
    """
    
    result = parse_date_added(sample_df)

    assert pd.api.types.is_datetime64_any_dtype(result["date_added"])
    assert result["month_added"].dtype == pd.Int64Dtype()
    assert result["year_added"].dtype == pd.Int64Dtype()


def test_parse_date_added_ne_modifie_pas_l_original(sample_df):
    """
    Vérifier que la fonction parse_date_added ne modifie pas le DataFrame original.

    :param sample_df: DataFrame d'exemple.
    """

    original_df = sample_df.copy()

    _ = parse_date_added(sample_df)

    pd.testing.assert_frame_equal(sample_df, original_df)
