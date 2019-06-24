def TriSelection(S):
    """ Tri par sélection

    Le tableau est constitué de deux parties : la 1ère constituée des éléments triés
    (initialisée avec seulement le 1er élément) et la seconde constituée des éléments
    non triés (initialisée du 2ème au dernier élément) """

    for i in range(0, len(S)-1):
        # rechercher l'élément le plus petit dans la partie du tableau restant non trié
        k = i
        for j in range(i+1, len(S)):
            if (S[j] <= S[k]):
                k = j

        # permuter cet élément et le premier élément dans le tableau non trié
        z = S[i]
        S[i] = S[k]
        S[k] = z

        # le tableau trié prend un élément de plus
        # le tableau non trié perd un élément

def TriInsertion(S):
    """ Tri par insertion

    Le tableau est constitué de deux parties : la 1ère constituée des éléments triés
    (initialisée avec seulement le 1er élément) et la seconde constituée des éléments
    non triés (initialisée du 2ème au dernier élément) """

    for i in range(0, len(S)-1):
        # Mémorisation du 1er élément de la partie du tableau non trié que nous
        # allons déplacer
        valeur = S[i+1]

        # Recherche de l'indice que doit prendre ce 1er élément dans la partie du
        # tableau trié
        indice = 0
        while S[indice] < valeur:
            indice += 1

        # Décalage des éléments compris entre le dernier élément de la partie
        # du tableau trié et l'emplacement trouvé précédemment (parcours décroissant)
        for j in range(i, indice-1, -1):
            S[j+1] = S[j]

        # Déplacement par insertion du 1er élément de la partie du tableau non trié
        # à l'indice trouvé ... qui devient un élément trié
        S[indice] = valeur