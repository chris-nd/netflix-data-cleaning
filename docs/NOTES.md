# Notes sur le nettoyage des données Netflix

## Gestion des valeurs manquantes

### La règle générale

le type cible de la colonne détermine les stratégies d'imputation disponibles.

- Une colonne texte peut recevoir "Unknown", "Not Specified", etc.

- Une colonne numérique peut recevoir une `moyenne` ou une `médiane` ou `0`.

- Une colonne date ne peut recevoir qu'une vraie date valide, NaT, ou rien du tout (laissé tel quel avant conversion).

- Mélanger les familles de types dans une même colonne casse tout en aval.

> Pour director, cast et country, j'ai choisi une imputation uniforme par `Not Specified` plutôt qu'une distinction par type, pour rester simple à ce stade du projet — la distinction ajouterait de la complexité (valeurs différentes, logique conditionnelle) sans bénéfice clair pour l'usage actuel (entraînement + dashboard basique). Limite assumée : un filtre futur sur director == "Not Specified" mélangera des films sans réalisateur identifié et des séries TV où le concept ne s'applique structurellement pas — à corriger si un usage plus fin en a besoin plus tard.

| Colonne    | % manquant | Mécanisme                                               | Décision provisoire            |
| ---------- | ---------- | ------------------------------------------------------- | ------------------------------ |
| director   | 30%        | MAR fort (91% des TV Show)                              | imputer "Not Specified"        |
| cast       | 9,4%       | MAR fort (76% docs/docuseries)                          | imputer "Not Specified"        |
| country    | 9,4%       | MAR faible (co-occurrence avec director/cast manquants) | imputer "Not Specified"        |
| date_added | 0,1%       | laissé tel quel                                         | deviendra NaT après conversion |
| rating     | 0,08%      | ponctuel, pas de pattern                                | Imputer "Unknown"              |
| duration   | 0%         | bug de décalage, corrigé                                | Fixé                           |
