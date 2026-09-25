# Publier l'extension sur les trois boutiques

Ce document décrit, boutique par boutique, ce qu'il faut fournir et ce que vous devez faire personnellement.

Les textes à copier se trouvent dans `LISTING.md`. La politique de confidentialité se trouve dans `POLITIQUE-CONFIDENTIALITE.md`.

---

## 1. À faire avant toute soumission

Ces quatre points bloquent les trois boutiques. Ils relèvent de vos décisions.

### 1.1 Trancher la question de la marque PRONOTE

PRONOTE est une marque déposée d'Index Éducation. Les trois boutiques refusent les fiches qui laissent croire à un lien officiel avec un éditeur tiers.

Fait : l'extension s'appelle désormais **Moyennes pour PRONOTE**, formulation de compatibilité, et chaque fiche se termine par une mention d'indépendance.

Reste à vérifier : les conditions d'utilisation d'Index Éducation, qui peut s'opposer à l'usage de sa marque. C'est le principal risque de refus, ou de retrait après publication.

### 1.2 Politique de confidentialité publiée

Fait. Elle est en ligne via GitHub Pages :

```
https://spartisperso.github.io/moyennes-pour-pronote/confidentialite.html
```

### 1.3 Adresse d'assistance

Fait : `spartis.dev@outlook.com`, et le site d'assistance est `https://spartisperso.github.io/moyennes-pour-pronote/`.

### 1.4 Vérifier la couverture des établissements

L'extension ne s'active que sur `https://*.index-education.net/pronote/*`. Les établissements qui hébergent PRONOTE sur leur propre nom de domaine ne sont pas couverts. À indiquer dans la description, ou à élargir dans le manifeste — un élargissement augmente toutefois le niveau d'examen des boutiques.

---

## 2. Paquets à fournir

Reconstruire les paquets après toute modification :

```
python tools\build_packages.py
```

| Boutique | Fichier |
| --- | --- |
| Chrome Web Store | `dist/moyennes-pour-pronote-chrome-edge.zip` |
| Microsoft Edge Add-ons | `dist/moyennes-pour-pronote-chrome-edge.zip` |
| Firefox (AMO) | `dist/moyennes-pour-pronote-firefox.zip` |
| Installation manuelle (GitHub) | `dist/Moyennes-pour-PRONOTE.zip` |

Le paquet Firefox est identique, à une exception près : il contient l'identifiant `browser_specific_settings.gecko.id`, **obligatoire** pour tout Manifest V3 soumis à AMO.

## 3. Visuels disponibles

| Fichier | Usage |
| --- | --- |
| `store/logo-300.png` | Logo de la fiche Edge (obligatoire), utilisable pour Chrome |
| `store/screenshot-1-par-matiere.png` | Capture 1280 × 800 (données fictives) |
| `store/screenshot-2-chronologique.png` | Capture 1280 × 800 (données fictives) |
| `store/promo-440x280.png` | Petite tuile promotionnelle (facultative) |
| `store/promo-1400x560.png` | Grande tuile promotionnelle (facultative) |
| `extension/icons/icon-128.png` | Icône de l'extension, lue dans le manifeste |

Les captures utilisent des données inventées : aucune donnée réelle d'élève n'est publiée.

---

## 4. Chrome Web Store

### Compte

Compte développeur Google : `spartis@gmail.com`, frais d'inscription réglés.

À savoir : un nouveau compte éditeur est limité à **deux extensions publiées**. Une augmentation peut être demandée plus tard.

### Soumission

1. **Add new item**, puis téléverser `dist/moyennes-pour-pronote-chrome-edge.zip`.
2. Onglet **Store Listing** : nom, résumé court (132 caractères maximum), description longue, catégorie, langue (français), captures 1280 × 800, tuiles promotionnelles facultatives.
3. Onglet **Privacy** :
   - **Single purpose** : texte fourni dans `LISTING.md` ;
   - **Permission justification** : justifier le script de contenu ;
   - **Data usage** : ne cocher aucune catégorie de collecte, puis cocher les trois certifications ;
   - **Privacy policy URL** : l'adresse publique préparée au point 1.2.
4. Onglet **Distribution** : gratuit, visibilité publique, pays de diffusion.
5. **Submit for Review**.

### Après soumission

- La publication peut être automatique après examen, ou différée manuellement.
- En cas de publication différée, vous disposez de **30 jours** pour publier, sinon la soumission repasse en brouillon.
- Un correctif avant fin d'examen se fait via **Cancel review**, puis nouveau téléversement.

---

## 5. Microsoft Edge Add-ons

### Compte

1. Créer un compte développeur sur [Partner Center](https://partner.microsoft.com/dashboard/microsoftedge/public/login) et s'inscrire au programme Edge. L'inscription au programme Edge est gratuite.

### Soumission

1. Espace **Edge**, puis **Create new extension**.
2. Téléverser `dist/moyennes-pour-pronote-chrome-edge.zip` (le paquet est validé automatiquement).
3. **Availability** : visibilité et marchés.
4. **Properties** : catégorie, et l'URL de la politique de confidentialité.
5. **Privacy** : déclarer l'objectif de l'extension, justifier le script de contenu, déclarer l'absence de code distant, certifier les pratiques de données.
6. **Store listings**, pour le français :
   - **Description** : minimum 250 caractères, maximum 10 000 ;
   - **Extension logo** : `store/logo-300.png`, format 1:1, 300 × 300 recommandé ;
   - **Screenshots** : 640 × 480 ou 1280 × 800, six maximum ;
   - **Tuiles promotionnelles** : 440 × 280 et 1400 × 560, facultatives ;
   - **Search terms** : liste fournie dans `LISTING.md`.
7. **Certification notes** : préciser qu'aucun compte de test n'est nécessaire, l'extension n'affichant rien tant qu'aucune page de notes PRONOTE n'est ouverte.
8. Soumettre.

À savoir : le **nom** et la **description courte** proviennent du manifeste. Pour les modifier, il faut reconstruire et re-téléverser le paquet.

---

## 6. Firefox (addons.mozilla.org)

### Compte

1. Créer ou utiliser un compte Mozilla, puis se rendre sur le [Developer Hub](https://addons.mozilla.org/developers/). La publication est gratuite.

Fait : compte créé avec `spartis.dev@outlook.com`.

### Soumission

1. **Submit a New Add-on**, puis choisir **On this site** pour une diffusion sur AMO.
2. Téléverser `dist/moyennes-pour-pronote-firefox.zip`. Le validateur signale immédiatement les erreurs.
3. **Source code** : répondre **non**. Le code n'est ni minifié ni compilé.
4. Page **Describe Add-on** :
   - nom, adresse de la fiche, résumé, description ;
   - deux catégories maximum ;
   - **e-mail et site d'assistance** ;
   - licence ;
   - politique de confidentialité ;
   - **Notes for Reviewers** : indiquer qu'aucun compte n'est nécessaire, et joindre la procédure de test ci-dessous.
5. **Submit Version**.

### Note à destination du relecteur AMO

```
L'extension n'a aucune permission et ne communique avec aucun serveur.
Elle s'active uniquement sur https://*.index-education.net/pronote/*.

Test sans compte PRONOTE : ouvrir le fichier tools/store-screenshot.html du dépôt,
qui reproduit la structure de la page de notes avec des données fictives et charge
le script de contenu. L'encart des moyennes doit apparaître au-dessus de la liste.
```

### Validation déjà effectuée

L'outil officiel de Mozilla a validé le paquet : **0 erreur, 0 avertissement, 0 notice**.

```
python tools\build_packages.py
node dist\webext\node_modules\web-ext\bin\web-ext.js lint --source-dir dist\firefox-source
```

Pour un essai visuel dans Firefox, avec un profil neuf et l'extension chargée :

```
node dist\webext\node_modules\web-ext\bin\web-ext.js run --source-dir dist\firefox-source
```

Connectez-vous à PRONOTE dans cette fenêtre, puis ouvrez **Notes > Les notes**.

---

## 7. Après publication

- Relever les trois adresses publiques et les ajouter au `README.md` et au guide d'installation.
- Le guide d'installation manuelle restera utile pour les versions non publiées et pour les tests.
- Toute nouvelle version se soumet en incrémentant `version` dans `extension/manifest.json`, puis en reconstruisant les paquets. Les trois boutiques refusent un numéro de version déjà soumis.

## 8. Récapitulatif de ce qui vous incombe

| Action | Pourquoi |
| --- | --- |
| Vérifier les conditions d'utilisation d'Index Éducation | Risque de refus ou de retrait lié à la marque |
| Créer le compte développeur Edge | Gratuit ; Chrome et Firefox sont déjà prêts |
| Soumettre et suivre les examens | Les délais varient d'une boutique à l'autre |
| Transmettre les adresses publiées | Pour ajouter les liens au dépôt et aux guides |
