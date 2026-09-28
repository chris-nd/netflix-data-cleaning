"Module pour la gestion des dates"

import pandas as pd


def parse_date_added(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convertit `date_added` en datetime et extrait le mois et 
    l'année dans ces colonnes respectives `month_added` et `year_added`.

    Choix de conception :
    - `errors='raise'` plutôt que `errors='coerce'` : avec `coerce`, 88 dates valides
    (espace en début de chaîne) étaient devenues NaT sans aucun signal.
    Un format inattendu doit faire échouer le pipeline, pas perdre des lignes.
    - Format explicite ('%B %d, %Y') plutôt qu'inféré : le contrat est lisible
      et ne dépend pas des premières lignes du fichier.
    - Les NaN d'origine (10 TV Show sans date) deviennent NaT sans erreur :
      c'est une absence structurelle, pas une conversion échouée.
    - `month_added` et `year_added` sont convertis en un type Int64 nullable 
      pour tolérer ces NaT.

    :param df: DataFrame contenant la colonne `date_added` en `str`.
    :return: copie du DataFrame avec `date_added` en datetime et deux colonnes ajoutées.
    :rtype: pd.DataFrame
    :raises ValueError: si une date ne respecte pas le format attendu.
    """

    df = df.copy()

    df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), format='%B %d, %Y', errors='raise')
    df['month_added'] = df['date_added'].dt.month.astype(pd.Int64Dtype())
    df['year_added'] = df['date_added'].dt.year.astype(pd.Int64Dtype())

    return df