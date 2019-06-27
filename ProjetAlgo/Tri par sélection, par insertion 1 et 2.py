def TriSelection(S):
    """ Tri par sélection

    Le tableau est constitué de deux parties : la 1ère partie constituée des éléments triés
    (initialisée vide) et la seconde partie constituée des éléments non triés (initialisée
    du 1er au dernier élément)

    """

    for i in range(0, len(S)-1):
        # initialiser l'indice de l'élément le plus petit avec l'indice du premier élément
        # de la partie du tableau non trié
        k = i

        # rechercher l'élément le plus petit dans la partie du tableau restant non trié
        for j in range(i+1, len(S)):
            if (S[j] < S[k]):
                k = j

        # permuter cet élément et le premier élément dans le tableau non trié
        z = S[i]
        S[i] = S[k]
        S[k] = z

        # le tableau trié prend un élément de plus à chaque itération
        # le tableau non trié perd un élément à chaque itération

def TriInsertion(S):
    """ Tri par insertion

    Le tableau est constitué de deux parties : la 1ère partie constituée des éléments triés
    (initialisée avec seulement le 1er élément) et la seconde partie constituée des éléments
    non triés (initialisée du 2ème au dernier élément)

    """

    for i in range(0, len(S)-1):
        # mémoriser le 1er élément de la partie du tableau non trié que nous
        # allons déplacer
        valeur = S[i+1]

        # rechercher l'indice que doit prendre ce 1er élément dans la partie du
        # tableau trié
        indice = 0
        while S[indice] < valeur:
            indice += 1

        # décaler les éléments compris entre le dernier élément de la partie
        # du tableau trié et l'emplacement trouvé précédemment (parcours décroissant)
        for j in range(i, indice-1, -1):
            S[j+1] = S[j]

        # déplacer (insérer) le 1er élément de la partie du tableau non trié
        # à l'indice trouvé ... qui devient un élément trié
        S[indice] = valeur

        # le tableau trié prend un élément de plus à chaque itération
        # le tableau non trié perd un élément à chaque itération

def TriInsertion2(S):
    """ Tri par insertion plus concis

    Le tableau est constitué de deux parties : la 1ère partie constituée des éléments triés
    (initialisée avec seulement le 1er élément) et la seconde partie constituée des éléments
    non triés (initialisée du 2ème au dernier élément)

    """

    for i in range(1, len(S)):
        # mémoriser le 1er élément de la partie du tableau non trié que nous
        # allons déplacer
        valeur = S[i]

        # initialisation de l'indice que doit prendre ce 1er élément dans la partie du
        # tableau trié
        indice = i

        # décaler les éléments compris entre le dernier élément de la partie
        # du tableau trié et l'emplacement souhaité (parcours décroissant)
        while indice >= 1 and valeur < S[indice-1]:
            S[indice] = S[indice-1]
            indice -= 1

        # déplacer (insérer) le 1er élément de la partie du tableau non trié
        # à l'indice trouvé ... qui devient un élément trié
        S[indice] = valeur

        # le tableau trié prend un élément de plus à chaque itération
        # le tableau non trié perd un élément à chaque itération