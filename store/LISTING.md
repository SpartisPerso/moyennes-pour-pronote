# Textes pour les fiches boutique

Ces textes sont à copier dans le Chrome Web Store, le Microsoft Edge Add-ons (Partner Center) et addons.mozilla.org (AMO).

---

## Nom

```
Moyennes pour PRONOTE
```

Ce nom est celui du manifeste : les fiches doivent utiliser exactement le même.

## Résumé court

Chrome : 132 caractères maximum. Edge : repris du champ `description` du manifeste. AMO : champ « Summary ».

```
Calcule vos moyennes dans PRONOTE lorsque l'établissement ne les affiche pas : moyenne par matière et moyenne générale.
```

118 caractères.

## Description longue

Edge exige au minimum 250 caractères. Le texte ci-dessous convient aux trois boutiques.

```
Moyennes pour PRONOTE affiche une estimation de la moyenne de chaque matière et de la moyenne générale, directement dans la page « Notes » de votre Espace PRONOTE.

À QUOI SERT CETTE EXTENSION

Certains établissements n'affichent pas les moyennes sur l'Espace Parents ou l'Espace Élèves. Plusieurs réglages de PRONOTE, décidés par l'établissement, peuvent en être la cause :
- l'option « Ne pas afficher la moyenne générale », activable pour tout l'établissement ;
- la date de publication du relevé de notes, qui contient les moyennes, souvent fixée en cours ou en fin de période ;
- la page « Relevé » qui peut ne pas être publiée sur les Espaces ;
- la publication des notes différée sur l'Espace Parents par rapport à l'Espace Élèves.

Ces choix visent fréquemment à limiter la comparaison entre élèves et le stress lié aux notes.

Si votre établissement affiche déjà les moyennes, cette extension ne vous sera d'aucune utilité : ce sont les valeurs officielles de PRONOTE qui font foi.

COMMENT ÇA MARCHE

L'extension lit uniquement les notes déjà affichées dans votre propre page, puis calcule la moyenne de chaque matière et la moyenne générale.

Deux méthodes de calcul sont proposées, au choix dans l'encart :
- « Pondérées par leur barème » (par défaut) : les points obtenus sont rapportés au total des points possibles, donc une note sur 10 compte moitié moins qu'une note sur 20. Avec 15,50/20 et 9,00/10, la moyenne vaut 16,33.
- « Toutes à poids égal » : chaque note est d'abord ramenée sur 20 et toutes comptent pareil. Avec les mêmes notes, la moyenne vaut 16,75.

Le choix est mémorisé pour votre établissement.

En affichage « Par ordre chronologique », un encart regroupe toutes les moyennes. En affichage « Par matière », la moyenne générale reste en haut et la moyenne de chaque matière s'affiche en face de son intitulé, alignée avec les notes.

IMPORTANT : UNE ESTIMATION, PAS UNE MOYENNE OFFICIELLE

L'extension applique un poids identique à chaque matière et ne connaît pas les coefficients des devoirs. PRONOTE, lui, applique les coefficients définis par les professeurs et l'établissement. Les résultats affichés sont donc une estimation, qui peut différer des moyennes officielles, notamment si des coefficients particuliers sont utilisés.

CONFIDENTIALITÉ

L'extension fonctionne entièrement dans votre navigateur. Elle ne collecte, n'enregistre et ne transmet aucune donnée. Elle ne demande aucune permission spéciale et n'utilise aucun serveur : aucune note ne quitte votre ordinateur.

L'extension s'active uniquement sur les pages PRONOTE hébergées sur index-education.net. Elle ne contourne aucune restriction d'accès et n'accède à aucune donnée qui ne serait pas déjà affichée à l'écran.

INDÉPENDANCE

Cette extension est un projet indépendant. Elle n'est ni éditée, ni approuvée, ni soutenue par Index Éducation, éditeur de PRONOTE. PRONOTE est une marque déposée d'Index Éducation.
```

## Avertissements à afficher

À reprendre dans la description et, si la boutique le permet, dans les notes de version :

- Les moyennes affichées sont une **estimation** calculée sans coefficients : elles peuvent différer des moyennes officielles de PRONOTE.
- L'extension **ne contourne aucune restriction** : elle recalcule uniquement à partir des notes déjà visibles par l'utilisateur connecté.
- Projet **indépendant d'Index Éducation**.
- En cas d'écart avec le bulletin, **seules les valeurs de l'établissement font foi**.

## Catégorie

- Chrome Web Store : `Workflow & Planning` (ou `Education` si proposé dans votre tableau de bord).
- Edge Add-ons : `Productivité`.
- AMO : `Other` en catégorie principale, `Bookmarks`/`Privacy` non pertinents ; choisir `Other`.

## Langue

Français (France). Une seule langue suffit pour une première publication.

## Termes de recherche

Non affichés aux utilisateurs, utilisés pour la découverte (Edge : champ dédié ; Chrome : intégrés à la description).

```
pronote, moyenne, moyennes, notes, bulletin, relevé, collège, lycée, parents, élèves
```

## Objectif unique (Chrome — champ « Single purpose »)

```
Calculer et afficher, dans la page Notes de l'Espace PRONOTE de l'utilisateur, une estimation de la moyenne par matière et de la moyenne générale, à partir des notes déjà affichées dans cette page.
```

## Justification des permissions

Le manifeste ne déclare **aucune permission** (`permissions` absent, pas de `host_permissions`). Seul un script de contenu est déclaré.

| Élément | Justification à saisir |
| --- | --- |
| Script de contenu sur `https://*.index-education.net/pronote/*` | L'extension doit lire les notes affichées dans la page PRONOTE de l'utilisateur pour y calculer et insérer les moyennes. Aucune donnée n'est extraite de la page ni transmise. |
| Code distant | Aucun. Tout le code est inclus dans le paquet. |

## Traitement des données (Chrome — onglet « Privacy », Edge — section confidentialité)

Répondre **non** à toutes les catégories de collecte : informations personnelles identifiables, informations de santé, informations financières, authentification, communications personnelles, localisation, historique de navigation, activité utilisateur, contenu de site web.

Certifications à cocher :

- je ne vends pas les données des utilisateurs à des tiers ;
- je n'utilise pas les données à des fins étrangères à l'objectif unique de l'extension ;
- je n'utilise pas les données pour évaluer la solvabilité ou accorder des prêts.

## Politique de confidentialité

URL publique à renseigner dans les trois boutiques :

```
https://spartisperso.github.io/moyennes-pour-pronote/confidentialite.html
```

Le texte source se trouve dans `POLITIQUE-CONFIDENTIALITE.md` et la page publiée dans `docs/confidentialite.html`.

## Marque PRONOTE — à trancher avant soumission

PRONOTE est une marque déposée d'Index Éducation. Les trois boutiques refusent les fiches laissant croire à un lien officiel avec l'éditeur.

Recommandations :

1. Le nom retenu est **« Moyennes pour PRONOTE »**, et non « PRONOTE Moyennes » : il marque la compatibilité, pas l'appartenance.
2. Conserver la mention d'indépendance en fin de description.
3. N'utiliser ni le logo, ni les couleurs, ni les captures de l'interface PRONOTE comme visuel principal de la fiche.
4. Vérifier les conditions générales d'utilisation d'Index Éducation, un éditeur pouvant s'opposer à l'usage de sa marque, même descriptif.

Ce point est le principal risque de refus ou de retrait ultérieur. Il relève d'une décision qui vous appartient.

## Assistance

- E-mail d'assistance : `spartis.dev@outlook.com`
- Site d'assistance : `https://spartisperso.github.io/moyennes-pour-pronote/`
- Dépôt du projet : `https://github.com/SpartisPerso/moyennes-pour-pronote`
