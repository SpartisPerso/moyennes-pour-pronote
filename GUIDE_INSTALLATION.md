# Guide d'installation pas à pas

Ce guide s'adresse aux personnes qui connaissent peu l'informatique. L'installation prend environ trois minutes et ne demande aucune commande à saisir.

> **À savoir avant d'installer.** Cette extension n'est utile que si votre établissement n'affiche pas les moyennes sur l'Espace Parents ou Élèves. Si les moyennes sont déjà visibles dans PRONOTE, ce sont elles qui font foi.

## 1. Télécharger le dossier

1. Cliquez sur [**Télécharger Moyennes pour PRONOTE**](https://github.com/SpartisPerso/moyennes-pour-pronote/releases/latest/download/Moyennes-pour-PRONOTE.zip).
2. Ouvrez le dossier **Téléchargements** de votre ordinateur.
3. Faites un clic droit sur **Moyennes-pour-PRONOTE.zip**, puis choisissez **Extraire tout**.
4. Cliquez sur **Extraire**.

Si le lien direct ne fonctionne pas, ouvrez la page des [versions disponibles](https://github.com/SpartisPerso/moyennes-pour-pronote/releases) et téléchargez **Moyennes-pour-PRONOTE.zip** dans la rubrique **Assets**.

## 2. Ouvrir le guide visuel

1. Ouvrez le dossier qui vient d'être extrait.
2. Double-cliquez sur **GUIDE_INSTALLATION.html**.
3. Le guide montre le sous-dossier **extension** à sélectionner.

Le sous-dossier **extension** est déjà prêt : aucun installateur et aucune copie dans AppData ne sont nécessaires. Conservez le dossier extrait après l'installation, car Edge utilise directement son contenu.

Le dossier extrait contient :

- **extension** (dossier à sélectionner dans Edge) ;
- GUIDE_INSTALLATION.html ;
- GUIDE_INSTALLATION.md ;
- README.md.

## 3. Autoriser l'installation locale dans Edge

1. Dans Edge, cliquez sur le bouton **Paramètres et plus** (les trois points, en haut à droite).
2. Choisissez **Extensions**, puis **Gérer les extensions**.
3. Sur la page **Extensions**, activez **Mode développeur**, en haut à droite.
4. Cliquez sur **Charger l'extension décompressée**.

Cette étape est imposée par Microsoft Edge pour toute extension qui n'est pas publiée dans la boutique Edge Add-ons.

## 4. Choisir le dossier déjà préparé

Une fenêtre intitulée **Sélectionner le répertoire d'extension** apparaît :

1. Rendez-vous dans le dossier **Moyennes-pour-PRONOTE** que vous avez extrait.
2. Cliquez une fois sur le dossier **extension** pour le sélectionner.
3. Cliquez sur **Sélectionner un dossier**.

La carte **Moyennes pour PRONOTE** doit maintenant apparaître dans le navigateur.

N'ouvrez pas le dossier **extension** : il suffit de le sélectionner. Ne choisissez ni le fichier ZIP, ni le dossier **Moyennes-pour-PRONOTE**.

## 5. Vérifier dans PRONOTE

1. Revenez dans PRONOTE.
2. Actualisez la page avec la touche `F5`.
3. Ouvrez **Notes**, puis **Les notes**.
4. Un encart **Moyennes estimées** apparaît au-dessus de la liste des notes.

En vue **Par ordre chronologique**, l'encart indique toutes les moyennes. En vue **Par matière**, la moyenne générale reste dans l'encart et chaque moyenne est alignée à droite avec les notes. Les notes sont ramenées sur 20, puis chaque matière compte de manière égale.

## En cas de problème

### Le bouton « Charger l'extension décompressée » n'apparaît pas

Vérifiez que **Mode développeur** est bien activé sur la page `edge://extensions`.

### L'extension est installée mais l'encart n'apparaît pas

1. Vérifiez que vous êtes dans **Notes > Les notes**.
2. Revenez sur `edge://extensions`.
3. Cliquez sur l'icône de rechargement de la carte **Moyennes pour PRONOTE**.
4. Revenez dans PRONOTE et appuyez sur `F5`.

### Mettre l'extension à jour

1. Téléchargez et extrayez la nouvelle version.
2. Sur `edge://extensions`, supprimez l'ancienne carte **Moyennes pour PRONOTE**.
3. Ouvrez le nouveau **GUIDE_INSTALLATION.html** et recommencez les étapes d'installation.
4. Actualisez PRONOTE avec `F5`.

### Désinstaller l'extension

1. Ouvrez `edge://extensions`.
2. Sur la carte **Moyennes PRONOTE**, cliquez sur **Supprimer**.

Vous pouvez ensuite supprimer le dossier extrait si vous ne souhaitez plus conserver les fichiers locaux.

## Confidentialité

L'extension lit uniquement les notes déjà affichées dans votre page PRONOTE. Elle n'envoie aucune donnée et ne demande aucune permission réseau.

Assistance : spartis.dev@outlook.com

Procédure Edge de référence : [documentation officielle Microsoft](https://learn.microsoft.com/microsoft-edge/extensions/getting-started/extension-sideloading).
