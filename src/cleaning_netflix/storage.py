"Entrées/sorties : lecture du CSV brut, écriture du CSV nettoyé."

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
RAW_PATH = ROOT / "data" / "raw" / "netflix_titles_raw.csv"
CLEAN_PATH = ROOT / "data" / "clean" / "netflix_titles_clean.csv"


def load_raw(path: Path = RAW_PATH) -> pd.DataFrame:
    """
    Charge le CSV brut tel quel, sans aucune transformation.

    :param path: Chemin vers le fichier CSV brut.
    :return: DataFrame.
    :rtype: pd.DataFrame
    """

    return pd.read_csv(path)


def save_clean(df: pd.DataFrame, path: Path = CLEAN_PATH) -> None:
    """
    Écrit le DataFrame nettoyé en CSV, en créant le dossier parent si besoin.

    :param df: DataFrame nettoyé.
    :param path: Chemin vers le fichier de sortie.
    """

    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
