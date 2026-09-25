# Analyse stratégique du catalogue Netflix

## Contexte métier

L'équipe Content Strategy souhaite répondre à plusieurs questions avant d'investir dans de nouveaux contenus :

* Quels types de contenus dominent le catalogue ?

* Quels pays produisent le plus de contenus disponibles sur Netflix ?

* Quels genres connaissent la plus forte croissance ?

* Quel est le délai moyen entre la sortie d'un contenu et son arrivée sur Netflix ?

* Existe-t-il des opportunités d'investissement dans certaines régions ?

Le livrable attendu est un dashboard Power BI accompagné d'un rapport analytique.

## Vue d'ensemble du workflow Data Analyst

![](data\:image/svg+xml;charset=utf-8,%3Csvg%20font-family%3D%22-apple-system-body%2C%20ui-sans-serif%2C%20-apple-system%2C%20system-ui%2C%20%26quot%3BSegoe%20UI%26quot%3B%2C%20Helvetica%2C%20%26quot%3BApple%20Color%20Emoji%26quot%3B%2C%20Arial%2C%20sans-serif%2C%20%26quot%3BSegoe%20UI%20Emoji%26quot%3B%2C%20%26quot%3BSegoe%20UI%20Symbol%26quot%3B%22%20font-weight%3D%22400%22%20data-d-component%3D%22svg%22%20fill%3D%22currentColor%22%20style%3D%22color%3Argb\(13%2C%2013%2C%2013\)%22%20viewBox%3D%220%200%20900%20140%22%20width%3D%22100%25%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Crect%20x%3D%2220%22%20y%3D%2240%22%20width%3D%22120%22%20height%3D%2250%22%20rx%3D%2210%22%20fill%3D%22none%22%20stroke%3D%22currentColor%22%2F%3E%3Ctext%20x%3D%2280%22%20y%3D%2270%22%20text-anchor%3D%22middle%22%20font-size%3D%2214%22%3EBusiness%3C%2Ftext%3E%3Cpath%20d%3D%22M140%2065%20H180%22%20stroke%3D%22currentColor%22%20stroke-width%3D%222%22%2F%3E%3Cpolygon%20points%3D%22180%2C65%20168%2C58%20168%2C72%22%20fill%3D%22currentColor%22%2F%3E%3Crect%20x%3D%22180%22%20y%3D%2240%22%20width%3D%22120%22%20height%3D%2250%22%20rx%3D%2210%22%20fill%3D%22none%22%20stroke%3D%22currentColor%22%2F%3E%3Ctext%20x%3D%22240%22%20y%3D%2270%22%20text-anchor%3D%22middle%22%20font-size%3D%2214%22%3ECollecte%3C%2Ftext%3E%3Cpath%20d%3D%22M300%2065%20H340%22%20stroke%3D%22currentColor%22%20stroke-width%3D%222%22%2F%3E%3Cpolygon%20points%3D%22340%2C65%20328%2C58%20328%2C72%22%20fill%3D%22currentColor%22%2F%3E%3Crect%20x%3D%22340%22%20y%3D%2240%22%20width%3D%22120%22%20height%3D%2250%22%20rx%3D%2210%22%20fill%3D%22none%22%20stroke%3D%22currentColor%22%2F%3E%3Ctext%20x%3D%22400%22%20y%3D%2270%22%20text-anchor%3D%22middle%22%20font-size%3D%2214%22%3ESQL%3C%2Ftext%3E%3Cpath%20d%3D%22M460%2065%20H500%22%20stroke%3D%22currentColor%22%20stroke-width%3D%222%22%2F%3E%3Cpolygon%20points%3D%22500%2C65%20488%2C58%20488%2C72%22%20fill%3D%22currentColor%22%2F%3E%3Crect%20x%3D%22500%22%20y%3D%2240%22%20width%3D%22120%22%20height%3D%2250%22%20rx%3D%2210%22%20fill%3D%22none%22%20stroke%3D%22currentColor%22%2F%3E%3Ctext%20x%3D%22560%22%20y%3D%2270%22%20text-anchor%3D%22middle%22%20font-size%3D%2214%22%3EPython%20EDA%3C%2Ftext%3E%3Cpath%20d%3D%22M620%2065%20H660%22%20stroke%3D%22currentColor%22%20stroke-width%3D%222%22%2F%3E%3Cpolygon%20points%3D%22660%2C65%20648%2C58%20648%2C72%22%20fill%3D%22currentColor%22%2F%3E%3Crect%20x%3D%22660%22%20y%3D%2240%22%20width%3D%22120%22%20height%3D%2250%22%20rx%3D%2210%22%20fill%3D%22none%22%20stroke%3D%22currentColor%22%2F%3E%3Ctext%20x%3D%22720%22%20y%3D%2270%22%20text-anchor%3D%22middle%22%20font-size%3D%2214%22%3EPower%20BI%3C%2Ftext%3E%3C%2Fsvg%3E)

## Phase 1 — Compréhension du besoin métier (Business Understanding)

### Objectif

Transformer une question métier en problématique analytique.

#### Questions du Product Manager

| Question                             | Traduction analytique      |
| ------------------------------------ | -------------------------- |
| Quels contenus investir ?            | Analyse des tendances      |
| Quels pays performent ?              | Classement des producteurs |
| Les séries grandissent-elles ?       | Évolution temporelle       |
| Quels genres deviennent populaires ? | Croissance par catégorie   |

#### KPI à construire

* Nombre total de contenus

* % Films vs Séries

* Top 10 pays producteurs

* Top genres

* Durée moyenne des films

* Nombre moyen de saisons

* Temps moyen entre sortie et ajout Netflix

## Phase 2 — Collecte des données

### Source

* Dataset Kaggle Netflix Shows

* Format : CSV

* Taille : environ 3,4 Mo

* 8 807 lignes

* 12 colonnes

### Architecture

![](data\:image/svg+xml;charset=utf-8,%3Csvg%20font-family%3D%22-apple-system-body%2C%20ui-sans-serif%2C%20-apple-system%2C%20system-ui%2C%20%26quot%3BSegoe%20UI%26quot%3B%2C%20Helvetica%2C%20%26quot%3BApple%20Color%20Emoji%26quot%3B%2C%20Arial%2C%20sans-serif%2C%20%26quot%3BSegoe%20UI%20Emoji%26quot%3B%2C%20%26quot%3BSegoe%20UI%20Symbol%26quot%3B%22%20font-weight%3D%22400%22%20data-d-component%3D%22svg%22%20fill%3D%22currentColor%22%20style%3D%22color%3Argb\(13%2C%2013%2C%2013\)%22%20viewBox%3D%220%200%20800%20180%22%20width%3D%22100%25%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Crect%20x%3D%2240%22%20y%3D%2260%22%20width%3D%22140%22%20height%3D%2260%22%20rx%3D%2212%22%20fill%3D%22none%22%20stroke%3D%22currentColor%22%2F%3E%3Ctext%20x%3D%22110%22%20y%3D%2295%22%20text-anchor%3D%22middle%22%20font-size%3D%2214%22%3EKaggle%20CSV%3C%2Ftext%3E%3Cpath%20d%3D%22M180%2090%20H290%22%20stroke%3D%22currentColor%22%20stroke-width%3D%222%22%2F%3E%3Cpolygon%20points%3D%22290%2C90%20278%2C83%20278%2C97%22%20fill%3D%22currentColor%22%2F%3E%3Crect%20x%3D%22290%22%20y%3D%2260%22%20width%3D%22180%22%20height%3D%2260%22%20rx%3D%2212%22%20fill%3D%22none%22%20stroke%3D%22currentColor%22%2F%3E%3Ctext%20x%3D%22380%22%20y%3D%2295%22%20text-anchor%3D%22middle%22%20font-size%3D%2214%22%3EPostgreSQL%3C%2Ftext%3E%3Cpath%20d%3D%22M470%2090%20H580%22%20stroke%3D%22currentColor%22%20stroke-width%3D%222%22%2F%3E%3Cpolygon%20points%3D%22580%2C90%20568%2C83%20568%2C97%22%20fill%3D%22currentColor%22%2F%3E%3Crect%20x%3D%22580%22%20y%3D%2260%22%20width%3D%22180%22%20height%3D%2260%22%20rx%3D%2212%22%20fill%3D%22none%22%20stroke%3D%22currentColor%22%2F%3E%3Ctext%20x%3D%22670%22%20y%3D%2295%22%20text-anchor%3D%22middle%22%20font-size%3D%2214%22%3EPython%20%2F%20Power%20BI%3C%2Ftext%3E%3C%2Fsvg%3E)

## Phase 3 — Audit qualité des données

Avant toute analyse.

### Vérifications

#### Structure

```python
df.shape
df.info()
df.describe()
```

#### Valeurs manquantes

Le dataset contient notamment :

| Colonne    | Problème                   |
| ---------- | -------------------------- |
| director   | Beaucoup de valeurs nulles |
| cast       | Valeurs manquantes         |
| country    | Valeurs manquantes         |
| date_added | Quelques dates absentes    |
| duration   | Quelques anomalies         |

Ces problèmes sont documentés dans plusieurs analyses utilisant ce dataset.

#### Doublons

```python
df.duplicated().sum()
```

## Phase 4 — Nettoyage des données (Data Cleaning)

C'est souvent 50 à 70 % du travail d'un Data Analyst.

### Étape 1 — Standardiser les colonnes

```python
df.columns = df.columns.str.lower()
```

### Étape 2 — Nettoyer les espaces

```python
df["country"]=df["country"].str.strip()
```

### Étape 3 — Corriger les dates

```python
df["date_added"]=pd.to_datetime(df["date_added"])
```

### Étape 4 — Séparer la durée

Le champ `duration` mélange :

* `90 min`

* `3 Seasons`

On crée :

| Ancien    | Nouveau             |
| --------- | ------------------- |
| 90 min    | movie_duration = 90 |
| 3 Seasons | seasons = 3         |

```python
df["duration_value"]=df["duration"].str.extract(r'(\d+)').astype(float)
```

### Étape 5 — Gérer les pays multiples

Exemple :

> United States, Canada

On transforme en plusieurs lignes.

Avant

| title  | country     |
| ------ | ----------- |
| Film A | USA, Canada |
| Film A | USA         |
| Film A | Canada      |

Cette technique est largement utilisée sur ce dataset pour obtenir des statistiques fiables par pays.

## Phase 5 — Modélisation des données

Au lieu d'une seule table, on construit un modèle analytique.

### Schéma en étoile

![4 Database Schema Examples for Various Applications | Airbyte](https://images.openai.com/static-rsc-4/sypTcCcKkLpXZ09_4rwDYIx5OixhuWmr5257Nr3zZJURqh8PZfdDRnLC79MYCyFjKf9b4FEl-TqpZW3jwlTaoB0CKOvqFq6poPGZfpGqFwaIwoGrvYMs2yJyfAlYNTWd0PONwERVhC0q2HH_LyvWVH13RHUyZWz413gAkpGXEAk?purpose=inline)

#### Table Fact

`fact_titles`

* show_id

* release_year

* duration

* rating

#### Dimensions

* dim_country

* dim_genre

* dim_date

* dim_type

* dim_rating

Cette structure améliore les performances dans Power BI.

## Phase 6 — Analyse des données avec Pandas

Objectif : transformer le dataset brut en plusieurs tables logiques afin de faciliter les analyses et les visualisations.

### Étape 1 — Charger le dataset

```python
import pandas as pd

df = pd.read_csv("netflix_titles.csv")
```

Vérifier rapidement la structure :

```python
df.shape
df.info()
df.head()
```

Le dataset contient 8 807 contenus et 12 colonnes.

### Étape 2 — Créer la table principale (Fact Table)

La table fact_titles conserve une ligne par contenu.

```python
fact_titles = df[[
    "show_id",
    "type",
    "title",
    "release_year",
    "rating",
    "duration"
]].copy()
```

Aperçu :

| show_id | type  | title                | release_year |
| ------- | ----- | -------------------- | ------------ |
| s1      | Movie | Dick Johnson Is Dead | 2020         |

### Étape 3 — Construire les dimensions

#### Dimension Pays

Le champ country contient parfois plusieurs pays.

Avant :

| title  | country               |
| ------ | --------------------- |
| Film A | United States, Canada |

Transformation :

```python
dim_country = (
    df[["show_id", "country"]]
      .dropna()
      .assign(country=lambda x: x["country"].str.split(","))
      .explode("country")
)

dim_country["country"] = dim_country["country"].str.strip()
```

Résultat :

| show_id | country               |
| ------- | --------------------- |
| s1      | United States         |
| s1      | Canada                |

Cette méthode (split() + explode()) est une pratique standard pour analyser correctement les pays sur ce dataset.

#### Dimension Genres

Même logique.

```python
dim_genre = (
    df[["show_id", "listed_in"]]
      .assign(listed_in=lambda x: x["listed_in"].str.split(","))
      .explode("listed_in")
)

dim_genre["listed_in"] = dim_genre["listed_in"].str.strip()
```

Résultat :

| show_id  | listed_in     |
| -------- | ------------- |
| s1       | Documentaries |

#### Dimension Date

Créer une véritable dimension temporelle.

```python
df["date_added"] = pd.to_datetime(df["date_added"])

dim_date = pd.DataFrame({
    "date": df["date_added"].dropna().unique()
})

dim_date["date"] = pd.to_datetime(dim_date["date"])
dim_date["year"] = dim_date["date"].dt.year
dim_date["month"] = dim_date["date"].dt.month
dim_date["month_name"] = dim_date["date"].dt.month_name()
```

Cette table servira aux analyses chronologiques.

### Étape 4 — Séparer les films et les séries

Le champ duration mélange minutes et saisons.

Créer une valeur numérique.

```python
df["duration_value"] = (
    df["duration"]
      .str.extract(r"(\d+)")
      .astype(float)
)
```

Créer deux colonnes.

```python
df["movie_duration"] = df["duration_value"].where(df["type"] == "Movie")

df["seasons"] = df["duration_value"].where(df["type"] == "TV Show")
```

#### Exemple :

| type    | duration  | movie_duration   | seasons |
| ------- | --------- | ---------------- | ------- |
| Movie   | 95 min    | 95               | NaN     |
| TV Show | 3 Seasons | NaN              | 3       |

### Étape 5 — Créer des indicateurs métier

Délai avant arrivée sur Netflix

```python
df["delay"] = (
    df["date_added"].dt.year
    - df["release_year"]
)
```

#### Exemple :

| title  | release_year | date_added | delay |
| ------ | ------------ | ---------- | ----- |
| Film A | 2018         | 2020       | 2     |

### Étape 6 — Préparer les KPI avec Pandas

Plutôt que des requêtes SQL, utiliser groupby().

### Films vs Séries

```python
content_type = (
    df.groupby("type")
      .size()
      .reset_index(name="count")
)
```

### Top 10 pays

```python
top_countries = (
    dim_country.groupby("country")
               .size()
               .sort_values(ascending=False)
               .head(10)
               .reset_index(name="count")
)
```

### Contenus ajoutés par année

```python
titles_by_year = (
    df.groupby(df["date_added"].dt.year)
      .size()
      .reset_index(name="count")
      .rename(columns={"date_added": "year"})
)
Durée moyenne des films
average_duration = df["movie_duration"].mean()
```

### Étape 7 — Export vers Power BI

Exporter les tables préparées.

```python
fact_titles.to_csv("fact_titles.csv", index=False)
dim_country.to_csv("dim_country.csv", index=False)
dim_genre.to_csv("dim_genre.csv", index=False)
dim_date.to_csv("dim_date.csv", index=False)
```

## Phase 7 — Analyse exploratoire (EDA)

### Librairies

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

### Distribution des contenus

![Netflix Data Analysis — part 2: EDA with Pandas and Matplotlib | by Luchiana Dumitrescu | Women in Technology | Medium](https://images.openai.com/static-rsc-4/QJbBju9WLEgCztOni0UxtiwOdTlPyRukG7Gvcq0PYBUMAFzQ8uWOovQeuxZ2Xp-tRDqJ6olCm7p0-zzW1NhEk6DJHMpQms95dBMmoxyoIfuE0ozMTIadesyOW_VDGW_z3sISIuBCsWrdpTUDhA3ShzKX04Z1zn8AmZry2Qtrtz0?purpose=inline)

Objectif :

* dominance des films

* poids des séries

### Évolution annuelle

![# How I Visualized Netflix Data Using Python and Google Colab - Vansh Srivastava - Medium](https://images.openai.com/static-rsc-4/zyJXTMNDJUClgCZeH3_9D-ST1a9l-0BI3q73iAvjJk-fQDokyCWjMwDSi1aZQqlWry4AV7kAf6adIxARrDgvmuO-bOhKvgCu2NvHzpdvb_AVUxBAuEboxKCOypjR1ieZ1P35ZZGEamkz3kzts1dRxH9jzpqvom5ktXXFzOUtBoc?purpose=inline)

Questions :

* Quand Netflix accélère-t-il ?

* Quelle période connaît la plus forte croissance ?

### Top pays

![Data Visualization — Netflix Data Set | by Shashank Singhal | Analytics Vidhya | Medium](https://images.openai.com/static-rsc-4/IFAFu-q72SFUnSLvPJ8QVQoNMaGkya2QSImUUvBWG93QBWGguHnzCMtmVBQwDgp1WSu0a1KzKkRbioh_5z2EunikOsQZbJY-dZnTjM6M9HAxRjZ54jS94WVzhghAGmjHt6DXdvtrZz6ZQWbvj0nZhYqQCwHTUymf8XBPKlKeDoE?purpose=inline)

Objectif :

* identifier les marchés majeurs.

### Genres populaires

![Recommendation content engine for Netflix | by Ishita | Medium](https://images.openai.com/static-rsc-4/05R6hvRsM7k34QWb9c_vQ8ZALXG8vJfDtfe8VB_UWDgg9ISk2mfAZne1cq3-SnHlgoauRMWauEhkXVL5Q5nnJO-ZP7oc_zcI9eaml8pSEIBJtjsAFTXV-HW0CHgxQjBz-XZlkrgcIggsZvJe_CO65ZwXMhbuvLwFXl_e97XOFbE?purpose=inline)

Les genres sont multi-valués.

Il faut :

```python
df["listed_in"].str.split(",")
```

puis `explode()`.

### Heatmap

Croiser :

* année

* type

![Visualize data with QuickSight. Amazon QuickSight is a cloud-based… | by Basanagouda Patil | Medium](https://images.openai.com/static-rsc-4/GnLCGRysOhTtR0enx_9XxTcb-7-QXb8g_AXDbo9U0iDac8I5OGDd9F9XuN_IAE6w20hPHm_scZzb2Ad-OV0pgPFdZK03nTx83EvSf0CMUdHvMhUZTJu2__vUdvvHlQokYLY3sZE1nkijxlzFBWX_5Ml8vdty25twZ6dJ5PX7cSM?purpose=inline)

## Phase 8 — Création de nouvelles variables

Les meilleurs analystes créent des indicateurs.

### Exemple

Temps avant arrivée sur Netflix

date_added−release_yeardate\_added-release\_yeardate_added−release_year

```python
df["delay"] = df["date_added"].dt.year - df["release_year"]
```

Cet indicateur mesure la rapidité d'acquisition.

## Phase 9 — Construction des KPI

| KPI             | Calcul             |
| --------------- | ------------------ |
| Catalogue total | COUNT              |
| Films           | COUNT WHERE Movie  |
| Séries          | COUNT WHERE TV     |
| Pays actifs     | DISTINCT country   |
| Genres          | DISTINCT listed_in |
| Délai moyen     | AVG(delay)         |

## Phase 10 — Dashboard Power BI

![Netflix Content Analysis Dashboard: Visualizing 8,807 Titles | Nakshatra Agrawal posted on the topic | LinkedIn](https://images.openai.com/static-rsc-4/ZFLWmm6Op6Ztuio87rzNXaPq94Ebd1NW8e0yW596IJXZMLPn1u353kPNSB6p5mrk6qeHVcQegGQz3bjY-uW4gObE0Kb6hi0rzVhlFJ49u5vqI5ZCCebkGiwecRJCwpCy-ZxZpxvc0G-CApYXt4uOXpC_8wX47XU5kcJv3vyeMA4?purpose=inline)

#### Page 1 — Executive Summary

* KPI Cards

* Films vs Séries

* Carte mondiale

#### Page 2 — Analyse temporelle

* Courbe annuelle

* Histogramme des sorties

#### Page 3 — Pays

* Carte

* Top producteurs

#### Page 4 — Genres

* Treemap

* Bar Chart

#### Slicers

* Pays

* Genre

* Rating

* Année

* Type

## Phase 11 — Storytelling

Les données deviennent des recommandations.

### Exemple

Observation :

> Les États-Unis dominent le catalogue.

Question :

Pourquoi ?

Hypothèses :

* Production historique importante

* Accords de licence

* Marché principal

Autre observation :

> Les séries augmentent fortement après 2015.

Conséquence possible :

* succès du binge-watching

* investissement dans les Originals

## Phase 12 — Rapport final

Structure professionnelle

### 1. Contexte

Objectif business.

### 2. Source

Présentation du dataset.

### 3. Nettoyage

Toutes les transformations.

### 4. Analyses

Graphiques.

### 5. Insights

Exemple :

* Les films représentent environ 70 % du catalogue.

* Les États-Unis et l'Inde figurent parmi les principaux pays producteurs.

* L'expansion du catalogue s'accélère fortement à partir de la seconde moitié des années 2010.

### 6. Recommandations

* cibler certains marchés émergents

* renforcer certains genres

* optimiser l'acquisition récente

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

* `data/` : uniquement des fichiers de données (CSV), jamais de code ni de notebook.

* `notebooks/` : uniquement des .ipynb, séparés par intention (exploration = jetable/brouillon, cleaning = final/documenté).

* `src/` : uniquement du code Python réutilisable, zéro exploration, zéro affichage de debug — importable ailleurs (ex: futur dashboard).

* `tests/` : miroir de src/, un fichier de test par module.
