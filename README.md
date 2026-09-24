# Cleaning Netflix Dataset

## Description

Ce projet a pour but de nettoyer le dataset Netflix pour le rendre utilisable pour des analyses ultérieures.

## Structure

```text
cleaning-netflix/
├── data/
│   ├── raw/
│   │   └── netflix_titles.csv       # jamais modifié après téléchargement
│   └── clean/
│       └── netflix_titles_clean.csv # généré par le notebook cleaning
├── notebooks/
│   ├── exploration.ipynb            # brouillon, hypothèses, tâtonnement
│   └── cleaning.ipynb               # linéaire, appelle src/, décisions finales
├── src/
│   └── cleaning_netflix/
│       ├── __init__.py
│       ├── io.py                    # load_raw(), save_clean()
│       ├── missing_values.py        # stratégies par colonne
│       ├── types.py                 # parsing duration (types mixtes)
│       └── dates.py                 # parsing date_added
├── tests/
│   └── test_*.py                    # pytest, un fichier par module de src/
├── .gitignore
├── .python-version
├── pyproject.toml
└── README.md
```

### La règle par dossier

- `data/` : uniquement des fichiers de données (CSV), jamais de code ni de notebook.

- `notebooks/` : uniquement des .ipynb, séparés par intention (exploration = jetable/brouillon, cleaning = final/documenté).

- `src/` : uniquement du code Python réutilisable, zéro exploration, zéro affichage de debug — importable ailleurs (ex: futur dashboard).

- `tests/` : miroir de src/, un fichier de test par module.
