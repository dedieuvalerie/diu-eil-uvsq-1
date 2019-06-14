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

