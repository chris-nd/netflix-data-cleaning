"""Enchaînement des étapes de nettoyage."""

import pandas as pd

from cleaning_netflix.column_types import split_duration
from cleaning_netflix.dates import parse_date_added
from cleaning_netflix.missing_values import clean_missing_values


def clean_netflix(df: pd.DataFrame) -> pd.DataFrame:
    """
    Applique le nettoyage complet dans un ordre imposé.

    L'ordre compte : `clean_missing_values` répare d'abord le décalage
    rating/duration (cas Louis C.K.). `split_duration` a besoin d'une
    `duration` réparée, sinon ces lignes resteraient sans durée.
    """

    df = clean_missing_values(df)
    df = split_duration(df)
    df = parse_date_added(df)
    return df
