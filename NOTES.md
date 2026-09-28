# Notes de nettoyage — Netflix Movies and TV Shows

## Contexte

Dataset Kaggle (8807 lignes, 12 colonnes) nettoyé avec Pandas.
Pipeline : `cleaning_netflix.pipeline.clean_netflix()`, testé (`pytest`),
orchestré depuis `notebooks/cleaning.ipynb`.

## Valeurs manquantes

| Colonne      | % manquant                       | Mécanisme                                                  | Décision |
|--------------|----------------------------------|------------------------------------------------------------|---|
| `director`   | 30%                              | MAR fort (91% des TV Show vs 3% des Movie) | `"Not Specified"` |
| `cast`       | 9,4%                             | MAR fort (76% documentaires/docuséries) | `"Not Specified"` |
| `country`    | 9,4%                             | MAR faible (co-occurrence avec director/cast manquants) | `"Not Specified"` |
| `rating`     | 0,08% (7 lignes)                 | ponctuel, pas de pattern | `"Unknown"`                                           |
| `duration`   | 0% (corrigé)                     | bug de décalage de colonnes (3 lignes Louis C.K. : la durée était dans `rating`) | valeur déplacée vers `duration`, `rating` réimputé |
| `date_added` | 0,1% (10 lignes, toutes TV Show) | absence structurelle liée au type | laissé tel quel → `NaT` après conversion |

**Compromis assumé sur `director`/`cast`/`country`** : imputation uniforme plutôt que distinguée par `type`. Un `TV Show` sans réalisateur crédité n'est pas dans la même situation qu'un `Movie` sans réalisateur (absence structurelle vs vrai manque de collecte), mais la distinction a été jugée trop complexe pour l'usage actuel (entraînement + dashboard simple). Limite : un futur filtre sur `director == "Not Specified"` mélangera les deux cas.

## Types mixtes — `duration`

Séparée en deux colonnes numériques indépendantes (principe tidy data : minutes et saisons ne sont pas la même variable) :

- `duration_minutes` (float, NaN pour les TV Show)
- `duration_seasons` (float, NaN pour les Movie)

Colonne `duration` originale supprimée après extraction (redondante, traçabilité conservée via `data/raw/`).

## Dates — `date_added`

- Format explicite (`%B %d, %Y`) plutôt qu'inféré, avec `errors='raise'`.
- Choix motivé par un bug rencontré : `errors='coerce'` transformait silencieusement 88 dates valides (espace en début de chaîne) en `NaT`, sans aucun signal.
- `year_added` / `month_added` extraites en `Int64` nullable.

## Limite connue : export CSV

Le format CSV ne conserve pas les types. Après rechargement :

- `date_added` redevient `str`
- `month_added`, `year_added`, `duration_minutes`, `duration_seasons` redeviennent `float64` (perte du nullable `Int64`)

Un futur usage du CSV nettoyé doit reconvertir ces colonnes explicitement (`parse_dates`, `dtype=` dans `pd.read_csv`), ou passer par un format qui conserve les types (Parquet).

## Principe général appliqué

Ne jamais supprimer une ligne entière à cause d'une seule colonne problématique quand le reste de la ligne reste exploitable. `dropna()` est un dernier recours, pas un réflexe.
