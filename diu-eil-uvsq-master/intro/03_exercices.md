# Exercices de base en Python
## Installation de l'environnement
-   Sous Linux, il est préférable d’utiliser le système de paquets de l’OS
    -   [python3](https://packages.debian.org/stretch/python3),
        [ipython3](https://packages.debian.org/stretch/ipython3),
        [python3-pip](https://packages.debian.org/stretch/python3-pip),
        [jupyter-notebook](https://packages.debian.org/stretch/jupyter-notebook)
        sous Debian,
    -   [python3](http://packages.ubuntu.com/bionic/python3),
        [ipython3](http://packages.ubuntu.com/bionic/python3),
        [python3-pip](http://packages.ubuntu.com/bionic/python3-pip),
        [jupyter-notebook](https://packages.ubuntu.com/bionic/jupyter-notebook)
        sous Ubuntu
-   Sous Windows, il suffit d’installer une distribution comme [Anaconda](https://www.continuum.io/anaconda-overview)
-   Sous Mac OS X, utiliser [Homebrew](https://brew.sh/).
    La procédure est détaillée sur la page [Installing Python 3 on Mac OS X](http://python-guide-pt-br.readthedocs.io/en/latest/starting/install3/osx/).
    La distribution [Anaconda](https://www.continuum.io/anaconda-overview) est également disponible sous Mac OS X.

1.  Vérifiez l’installation en reproduisant les instructions des sections
    [Lancer un interpréteur interactif](02_python_refCard.md#repl) et
    [Lancer un notebook Jupyter](02_python_refCard.md#notebook).

## Création d’un compte github
Les plateformes comme [Github](https://github.com/) permettent d’héberger des projets en utilisant un système de gestion de versions ([git](https://git-scm.com/)).
1.  Créez-vous un compte sur [Github](https://github.com/).
1.  Faites un *fork* du dépôt <https://github.com/hal91190/diu-eil-uvsq.git> dans votre espace.
1.  Cloner localement votre nouveau dépôt.

## Premiers pas en Python
Dans cette section, vous utiliserez comme base le répertoire [`intro/src`](src) des sources du cours.
N’hésitez pas à faire des modifications dans les exemples proposés.
1.  Exécutez le script [`first_script.py`](first_script.py) de la section *Exemple de script Python*.
    Vous pouvez également exécuter le script [`first_import.py`](first_import.py) pour mettre en évidence les différences entre exécution et importation.
1.  Dans un notebook, ouvrez (ou reproduisez) et exécutez le fichier [`Python RefCard.ipynb`](src/python_refCard.ipynb) qui reprend les exemples du cours.
1.  Répondez aux questions suivantes
    1.  Dans la documentation du langage, où se trouve la documentation de la fonction `print` (pour Python 3.7, pour Python 2.7) ? Même question pour l’instruction `print` de Python 2.7.
    1.  Où se trouve la documentation de l’instruction `assert` ?
    1.  Quelle convention utilise-t-on pour nommer les fonctions en Python ?
    1.  En dehors de la classe `str`, quels modules de la bibliothèque standard permettent de manipuler du texte ?
    1.  Dans l’index [PyPI](https://pypi.python.org/pypi), combien de bibliothèques sont liées au thème *Games/Entertainment* pour la version 3.6 de Python ?
    1.  En Python 3, quelle est la différence entre les opérateurs `/` et `//` ?
    1.  En utilisant les listes en compréhension, générer les tables de multiplication jusqu’à 10.

## Réalisation d'une leçon sur les bases du langage
Le but est ici de réaliser un notebook présentant une notion de base du langage Python.
Le notebook doit être conçu comme une progression permettant à un élève d'acquérir cette notion.
Il contiendra des explications et des questions/exercices à réaliser.

La liste ci-dessous propose quelques thèmes que vous pouvez aborder :
- **Fonctions** : passage des paramètres, paramètres par défaut, fonctions natives (print, range, ...)
- **Opérateurs** : opérateurs arithmétiques, concaténation
- **Structure d'un programme** : indentation, blocs d'instructions, importations
- **Structures de contrôle** : boucles, conditions
- **Typage** : typage fort mais dynamique (notion de type associée à l'objet et pas à l'identificateur), duck typing
- **Types de base** : int, float, str, bool
- **Variables** : référence (couple identificateur/objet référencé), mutable/non mutable, identité des objets
