# Python RefCard
## Le langage Python
-   Créé en 1990 par Guido Van Rossum
-   Caractéristiques
    -   compilé/interprété
    -   langage de scripts
    -   système de typage implicite, dynamique, fort
    -   support de la programmation procédurale, OO, fonctionnelle (partiel)

> En 2019, deux versions incompatibles de Python co-existent ([2.7 et 3.7](https://wiki.python.org/moin/Python2orPython3))

## Quelques domaines d’application
-   Langage de scripts
-   Programmation scientifique
    -   analyse de données, bioinformatique (analyse du génôme)
-   Développement web
    -   plusieurs frameworks populaires
-   Développement d’outils pour le développement logiciel
-   Enseignement de l’informatique

## Implémentations
-   [CPython](https://fr.wikipedia.org/wiki/CPython) est l’implémentation de référence
-   Principales implémentations alternatives
    -   [Jython](http://www.jython.org/) pour la JVM,
    -   [IronPython](http://ironpython.net/) pour .Net,
    -   [PyPy](http://pypy.org/)

## Distributions
-   [Langage seul](https://www.python.org/downloads/)
-   Paquets sous Linux (
    [python](https://packages.debian.org/stretch/python)/
    [python3](https://packages.debian.org/stretch/python3) sous Debian,
    [python](http://packages.ubuntu.com/bionic/python)/
    [python3](http://packages.ubuntu.com/bionic/python3) sous Ubuntu,
    …​)
-   [Anaconda](https://www.continuum.io/anaconda-overview)
-   [ActivePython](https://www.activestate.com/activepython)
-   [Python(x,y)](http://python-xy.github.io/)
-   [Intel Distribution for Python](https://software.intel.com/en-us/intel-distribution-for-python)

## Quelques outils de développement
-   REPL :
    [IPython](https://ipython.org/)
-   Notebook :
    [Jupyter](https://jupyter.org/)
-   IDE :
    [Spyder](https://pythonhosted.org/spyder/),
    [PyCharm](https://www.jetbrains.com/pycharm/),
    [PyDev](http://www.pydev.org/),
    [Python pour VS Code](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python),
    [Python Tools for Visual Studio](https://microsoft.github.io/PTVS/)
-   Guide de style :
    [PEP 8](https://www.python.org/dev/peps/pep-0008/),
    [PEP 8 — the Style Guide for Python Code](http://pep8.org/),
    [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
-   Documentation :
    [pydoc](https://docs.python.org/3/library/pydoc.html)
-   Audit de code :
    [Pylint](https://www.pylint.org/)
-   Gestion des paquets :
    [pip](https://pip.pypa.io/en/stable/),
    [PyPI](https://pypi.python.org/pypihttps://pypi.python.org/pypi)
-   Environnement virtuel :
    [virtualenv](https://pypi.python.org/pypi/virtualenv),
    [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/),
    [pipenv](http://docs.pipenv.org/en/latest/)
-   Débogage :
    [pdb](https://docs.python.org/3/library/pdb.html)/
    [ipdb](https://github.com/gotcha/ipdb)
-   Tests unitaires :
    [unittest](https://docs.python.org/3/library/unittest.html)

## <a name="repl"></a>Lancer un interpréteur interactif
-   Lancer le REPL (sous Linux)
```
$ python3
Python 3.5.3rc1 (default, Jan  3 2017, 04:40:57)
[GCC 6.3.0 20161229] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
$
```
-   Lancer IPython (sous Linux)
```
$ ipython3
Python 3.5.3rc1 (default, Jan  3 2017, 04:40:57)
Type "copyright", "credits" or "license" for more information.

IPython 5.1.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: quit
$
```

## <a name="notebook"></a>Lancer un notebook Jupiter
-   Lancement sur <http://localhost:8888/>
```
$ jupyter-notebook
[I 09:55:27.102 NotebookApp] Writing notebook server cookie secret to /run/user/1000/jupyter/notebook_cookie_secret
[W 09:55:27.136 NotebookApp] Widgets are unavailable. On Debian, notebook support for widgets is provided by the package jupyter-nbextension-jupyter-js-widgets
[I 09:55:27.151 NotebookApp] Serving notebooks from local directory: /home/hal
[I 09:55:27.151 NotebookApp] 0 active kernels
[I 09:55:27.151 NotebookApp] The Jupyter Notebook is running at: http://localhost:8888/
[I 09:55:27.151 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
```
-   Arrêt en tapant deux fois Ctrl+C

## Exemple de script Python
**Fichier [`src/first_script.py`](src/first_script.py).**
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Ce module est un exemple simple de script Python.

    Un commentaire débute par # et se termine en fin de ligne.
    Un script débute par un shebang (optionnel).
    Le shebang est inutile dans le cas d'un module non exécuté directement
    La seconde ligne de commentaire précise l'encodage du fichier (optionnel).
    On trouve ensuite la docstring du module qui documente le module lui-même (optionnel).
"""

print(
    """
        Ce code est exécuté dans tous les cas.
    """)

if __name__ == '__main__':
    # L'indentation définit un bloc de code imbriqué
    print(
        """
            Ce bloc de code est exécuté uniquement quand le module est invoqué
            directement par l'interpréteur, i.e. pas importé
        """)
```

## Exécuter un programme Python
-   En appelant l’interpréteur
```
$ python3 intro/first_script.py

        Ce code est exécuté dans tous les cas.


            Ce bloc de code est exécuté uniquement quand le module est invoqué
            directement par l'interpréteur, i.e. pas importé
```
-   Directement par le shell (utilise le *shebang*)
```
$ chmod +x intro/first_script.py
$ intro/first_script.py
```

## Généralités
-   Commentaire introduit par `#`
-   Différence entre minuscules et majuscules
-   **L’indentation définit l’imbrication des blocs**
-   Pas de constante
    -   variable qu’on ne modifie pas
    -   par convention, nommée en majuscule et avec des `_`
-   Toutes les données sont représentées par des *objets*

## Principaux types prédéfinis 1/2
-   `numbers.Number` représente les nombres (immuables)
    -   `numbers.Integral` pour les entiers
        -   `int` nombre entier sans limite de taille
        -   `bool` possède les valeurs `True` et `False`
    -   `float` (`numbers.Real`) nombre en virgule flottante double précision
    -   `complex` (`numbers.Complex`) nombre complexe représenté comme une paire de `float`
-   `None` possède une seule valeur `None`
-   cf. [The standard type hierarchy](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy)

> Les exemples de cette section sont disponibles dans le notebook [`src/Python RefCard.ipynb`](src/Python%20RefCard.ipynb)

## Principaux types prédéfinis 2/2
-   Une *séquence* représente une collection ordonnée (indexée par des entiers)
    -   une *séquence immuable* ne change pas après sa création
        -   une *chaîne de caractère* est une séquence de caractères unicodes
        -   un *tuple* représente un n-uplet d’objets quelconques
    -   une *séquence mutable* supporte les modifications
        -   une *liste* est formée d’éléments quelconques
-   Un *ensemble* représente une collection non ordonnée d’éléments uniques
    -   un *ensemble* est modifiable
-   Un *dictionnaire* représente une collection modifiable de couples (clé, valeur)

## Littéraux
-   Un *littéral* est la représentation dans le code source d’une valeur d’un type
-   `int` : `1234`, `0b11001` en binaire, `0o177` en octal, `0xAFF` en héxa, `_` est permis (v 3.6)
-   `float` : `3.14`, `10.`, `.001`, `1e100`, `3.14e-10`
-   Imaginaire : littéral `float` suffixé par `j` construit un complexe de partie réelle nulle (`3+4j` pour une partie réelle non nulle)
-   Chaîne : `"chaîne"`, `'chaîne'`, `"""chaîne multi-lignes"""`, `'''chaîne multi-lignes'''`, préfixée par `r` pour éviter
    l’interprétation, par `f` pour une chaîne formatée (v. >= 3.6)

## Liaison des variables et référence
-   Les variables sont en fait des *références*
-   La valeur d’une telle variable est une référence vers (l’adresse de) une donnée
    -   dans d’autres langages, une référence est appelée *pointeur*
    -   dans les deux cas, ce sont des variables dont la valeur (le contenu) est une adresse mémoire
-   Une référence est une *abstraction* de plus haut niveau
    -   fournit une interface plus simple pour manipuler l’adresse
    -   ne permet pas de manipuler directement l’adresse mémoire
    -   un pointeur est un concept de bas-niveau permettant une manipulation directe de l’adresse (arithmétique des pointeurs,
        pointeur de fonction, …​)
-   L’association (l’affectation) d’une donnée à une variable *lie* l’identificateur et la donnée

## Structures de contrôle
-   `pass`
-   `if i < 10:`, `elif i > 100:`, `else:`
-   `while i < 10:`
-   `for idx in seq:`, `for i in range(0, 10, 3):`
-   `break`, `continue`, `else:` pour une boucle

> Il faut bien respecter l’indentation.

## Quelques opérateurs spécifiques
-   `/` représente la division en virgule flottante
-   `//` représente la division entière
-   `**` représente l’élévation à la puissance
-   `a if condition else b` est une expression conditionnelle
-   pas d’opérateur de conversion de types

> Certains opérateurs peuvent être surchargés pour certains types

## Fonction
-   Lors de l’appel, les paramètres formels sont liés aux arguments
-   Un appel de fonction retourne toujours une valeur (éventuellement `None`)
-   Les fonctions peuvent être imbriquées
```python
def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(2000) # Appel de la fonction
```

## Exemple de manipulation de chaînes
-   Une chaîne est une instance immuable de la classe [`str`](https://docs.python.org/3/library/stdtypes.html#textseq)
-   Le module [`string`](https://docs.python.org/3/library/string.html) complète les possibilités de manipulation de chaînes

```python
word = 3 * 'un' + 'ium' # 'unununium'
word[0]   # character in position 0
word[-1]  # last character
word[2:5] # characters from position 2 (included) to 5 (excluded)
word[:2]  # character from the beginning to position 2 (excluded)
word[4:]  # characters from position 4 (included) to the end
len(word) # size of the string
```

## Exemple de manipulation de tuples
-   Un tuple supporte les opérations sur les [séquences](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)
-   Un tuple est une instance immuable de la classe [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)

```python
t = () # tuple vide
t = 12345, # singleton
t = 12345, 54321, 'hello!'
t[0] # premier élément
```

## Exemple de manipulation de listes
-   Une liste supporte les opérations sur les [séquences](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)
-   Une liste est une instance de la classe [`list`](https://docs.python.org/3/library/stdtypes.html#list)

```python
squares = [1, 4, 9, 16, 25]
squares = [x**2 for x in range(10)] # liste en compréhension
del squares[0] # supprime le premier élément
cubes = [1, 8, 27, 65, 125]
cubes[3] = 64 # modifiable
del cubes # supprime la variable
```

## Exemple de manipulation d’ensembles
-   Un ensemble est une instance de la classe [`set`](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)

```python
basket = set() # ensemble vide
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
'orange' in basket # test d'appartenance
a = set('abracadabra') # les doublons sont éliminés
b = set('alacazam')
a - b # différence
a | b # union
a & b # intersection
a ^ b # a union b privé de a inter b
a = {x for x in 'abracadabra' if x not in 'abc'} # ensemble en compréhension
```

## Exemple de manipulation de dictionnaires
-   Un dictionnaire est une instance de la classe [`dict`](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

```python
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
del tel['sape']
```

## Références
-   [Site officiel](https://www.python.org/)
    -   [Tutoriel](https://docs.python.org/3/tutorial/index.html),
        [Référence du langage](https://docs.python.org/3/reference/index.html),
        [Référence de la bibliothèque standard](https://docs.python.org/3/library/index.html),
        [Guide de style](https://www.python.org/dev/peps/pep-0008/),
        [The Zen of Python](https://www.python.org/dev/peps/pep-0020/)
-   Page Wikipedia
    ([fr](https://fr.wikipedia.org/wiki/Python_%28langage%29),
    [en](https://en.wikipedia.org/wiki/Python_%28programming_language%29))
-   [Une introduction à Python 3](https://perso.limsi.fr/pointal/python:courspython3),
    [Mémento Python 3](https://perso.limsi.fr/pointal/python:memento),
    [Abrégé Dense Python 3.2](https://perso.limsi.fr/pointal/python:abrege), L. Pointal
-   [Apprenez à programmer en Python](https://openclassrooms.com/courses/apprenez-a-programmer-en-python), cours Open Classrooms
-   [Apprendre le langage de programmation python](https://apprendre-python.com/)
-   [The Hitchhiker’s Guide to Python!](http://python-guide-pt-br.readthedocs.io/en/latest/)
    ([fr](https://python-guide-fr.readthedocs.io/fr/latest/)), Kenneth Reitz (livre)
-   [Core Python](https://dzone.com/refcardz/core-python), DZone Refcard
-   [The Hitchhiker’s Guide to Packaging](https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/index.html)
-   [Dive Into Python 3](http://www.diveintopython3.net/), Mark Pilgrim (livre)
-   [Invent with Python](http://inventwithpython.com/), Albert Sweigart (livres)
-   [Program Arcade Games With Python And Pygame](http://programarcadegames.com/)
    ([fr](http://programarcadegames.com/index.php?lang=fr)), Paul Craven (livre)
