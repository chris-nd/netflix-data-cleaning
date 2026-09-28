"Module de test pour le module d'entrée/sortie"

import pandas as pd

from cleaning_netflix.storage import load_raw, save_clean


def test_load_raw_lit_le_csv(tmp_path):
    """
    Teste le chargement du fichier CSV brut.

    :param tmp_path: Chemin temporaire pour les fichiers de test
    """

    expected = pd.DataFrame(
        {
            "type": ["movie", "show"],
            "title": ["Movie 1", "Show 1"],
            "director": ["John Doe", "Jane Smith"],
            "cast": ["Actor 1", "Actor 2"],
            "country": ["USA", "Canada"],
            "date_added": ["2020-01-01", "2020-01-02"],
            "release_year": [2020, 2020],
            "rating": ["PG-13", "TV-MA"],
            "duration": ["90 min", "2 Seasons"],
            "listed_in": ["Dramas", "International Movies"],
            "description": ["Description 1", "Description 2"],
        }
    )

    file = tmp_path / "raw.csv"
    expected.to_csv(file, index=False)

    pd.testing.assert_frame_equal(load_raw(file), expected)


def test_save_clean_cree_le_dossier_et_ecrit(tmp_path):
    """
    Teste la sauvegarde du DataFrame nettoyé.
    :param tmp_path: Chemin temporaire pour les fichiers de test
    """

    df = pd.DataFrame(
        {
            "type": ["movie", "show"],
            "title": ["Movie 1", "Show 1"],
            "director": ["John Doe", "Jane Smith"],
            "cast": ["Actor 1", "Actor 2"],
            "country": ["USA", "Canada"],
            "date_added": ["2020-01-01", "2020-01-02"],
            "release_year": [2020, 2020],
            "rating": ["PG-13", "TV-MA"],
            "duration": ["90 min", "2 Seasons"],
            "listed_in": ["Dramas", "International Movies"],
            "description": ["Description 1", "Description 2"],
        }
    )

    out = tmp_path / "data" / "clean" / "out.csv"  # dossier inexistant

    save_clean(df, out)

    assert out.exists()
    pd.testing.assert_frame_equal(pd.read_csv(out), df)
