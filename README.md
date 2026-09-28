# Nettoyage du dataset Netflix

Nettoyage du dataset [Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)
avec Pandas : valeurs manquantes, types mixtes, dates — chaque décision justifiée
plutôt qu'un `dropna()` global. Voir [`NOTES.md`](./NOTES.md) pour le détail des
décisions et leurs justifications.

## Prérequis

- Python (version voir `.python-version`)
- [uv](https://docs.astral.sh/uv/)

## Installation

```bash
uv sync
```

### Récupérer le dataset

1. Télécharger `netflix_titles.csv` depuis [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)
2. Le placer dans `data/raw/netflix_titles.csv`

Le fichier brut n'est pas versionné (licence Kaggle, reproductibilité plutôt que stockage).

## Structure

```text
cleaning-netflix/
├── data/
│   ├── raw/
│   │   └── netflix_titles_raw.csv   # jamais modifié après téléchargement
│   └── clean/
│       └── netflix_titles_clean.csv # généré par le notebook cleaning
├── notebooks/
│   ├── exploration.ipynb            # brouillon, hypothèses, tâtonnement
│   └── cleaning.ipynb               # linéaire, appelle src/, décisions finales
├── src/
│   └── cleaning_netflix/
│       ├── __init__.py
│       ├── column_types.py          # load_raw(), save_clean()
│       ├── dates.py                 # load_raw(), save_clean()
│       ├── missing_values.py        # stratégies par colonne
│       ├── pipeline.py              # parsing duration (types mixtes)
│       └── storage.py               # parsing date_added
├── tests/
│   ├── test_column_types.py
│   ├── test_dates.py
│   ├── test_missing_values.py
│   ├── test_pipeline.py
│   └── test_storage.py
├── .gitignore
├── .python-version
├── NOTES.md
├── pyproject.toml
├── README.md
└── uv.lock
```

### La règle par dossier

- `data/` : uniquement des fichiers de données (CSV), jamais de code ni de notebook.

- `notebooks/` : uniquement des .ipynb, séparés par intention (exploration = jetable/brouillon, cleaning = final/documenté).

- `src/` : uniquement du code Python réutilisable, zéro exploration, zéro affichage de debug — importable ailleurs (ex: futur dashboard).

- `tests/` : miroir de src/, un fichier de test par module.

## Utilisation

```bash
uv run jupyter lab notebooks/cleaning.ipynb   # exécuter le nettoyage
uv run pytest                                  # lancer les tests
```

Le CSV nettoyé est généré dans `data/clean/netflix_titles_clean.csv`.

## Remerciements

- [Shivam Bansal](https://www.kaggle.com/shivamb) pour avoir partagé ce dataset sur Kaggle.
- [Roadmap.sh](https://roadmap.sh/projects/cleaning-netflix-dataset) pour avoir mis à disposition ce projet de nettoyage de dataset.
