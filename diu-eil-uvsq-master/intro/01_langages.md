# Caractéristiques des langages de programmation

## Implémentation des langages
-   Avec un [*langage compilé*](https://en.wikipedia.org/wiki/Compiled_language), le code source du programme est transformé en *code machine* par le *compilateur*
-   Dans un [*langage interprété*](https://en.wikipedia.org/wiki/Interpreted_language), le code source du programme est exécuté "à la volée" par l'*interpréteur*
-   Certains langages sont à la fois compilés et interprétés
-   Il existe des approches intermédiaires (compilation *Just In Time* (JIT))

### C est compilé
**Compilation séparée (produit `util.o` et `main.o`).**
```
$ gcc -c util.c
$ gcc -c main.c
```

**Édition de liens (produit `monprog`).**
```
$ gcc -o monprog main.o util.o
```

**`monprog` est exécutable.**
```
$ ./monprog
```

### PHP est interprété
**Exécution d’un programme PHP.**
```
$ php monprog.php
```

### Java est compilé puis interprété (JIT)
**Compilation en *bytecode* (produit `Main.class`).**
```
$ javac Main.java
```

**Exécution avec la JVM (*Java Virtual Machine*).**
```
$ java Main
```

### Langage de scripts
-   Un *script* est un programme destiné à automatiser l’enchaînement de tâches dans un environnement particulier
-   Un *langage de scripts* est un langage de programmation permettant de développer des scripts
-   Il permet d’invoquer les primitives du système sous-jacent
-   Il dispose en général d’un *REPL* (*Read-Eval-Print Loop*)
-   Quelques exemples
    -   shells pour les OS : Bash, Zsh, tcsh
    -   ECMAScript (Javascript) pour les navigateurs web
    -   Lua embarqué dans une application (*VLC Media Player*, jeu *Battle for Wesnoth*)

## Système de typage
-   Un *système de typage* attribue des types aux éléments du langage
-   Attribuer un type à une expression permet de limiter les erreurs de programmation
    -   en définissant ce qu’il est possible de faire avec une expression
    -   en définissant les règles de compatibilité entre expressions
    -   en vérifiant ces contraintes

### Typage explicite vs. implicite
-   Le typage est *explicite* si les annotations de type sont visibles dans le code source

**En C, chaque déclaration de variable précise son type.**
```c
int nombre = 1;
double pi = 3.141592;
```

-   Le typage est *implicite* si les types ne sont pas précisés dans le code source

**En PHP, la première affectation crée la variable.**
```php
$nombre = 1;
$pi = 3.141592;
```

-   Des langages à typage explicite peuvent faire appel à l'*inférence de types* dans certaines situations
    -   permet la déduction automatique des types

**En Java 10, on peut omettre le type pour les variables locales (mot-vlé `var`).**
```java
var listofMovies = new HashMap<User,List<String>>();
```

### Typage statique vs. dynamique
-   Le typage est *statique* si l’information de type est associée à l’identificateur
    -   ⇒ la vérification des types peut être réalisée lors de la compilation
-   Le typage est *dynamique* si l’information de type est portée par l’objet lui-même
    -   ⇒ la vérification se fait durant l’exécution

### Typage statique
-   Améliore la fiabilité du programme (plus de vérifications plus précoces)
-   Meilleur support des outils (IDE)
-   Meilleures performances

**En C, les erreurs de type sont identifiées par le compilateur.**
```c
double a = "une chaine";
// error: incompatible types when initializing type ‘double’ using type ‘char *’
```

### Typage dynamique
-   Offre plus de souplesse dans l’écriture du code source
    -   *duck typing*, *data as code*, métaprogrammation
-   Permet le prototypage rapide

**En PHP, les erreurs de type peuvent passer inaperçues.**
```php
$a = 1;
$a = "une chaine";
echo $a + 2; // affiche 2
```

### Typage fort vs. faible
-   Le typage est *fort* si les manipulations entre données de types différents sont limitées et contrôlées
-   Le typage est *faible* si les possibilités de transtypage sont nombreuses et implicites
-   Ces notions sont relativement floues

**Le C est à typage fort mais…​.**
```c
int a = "une chaine";
printf("%d\n", a); // 443215...
```

## Support des paradigmes de programmation
-   Un **paradigme de programmation** représente la façon d’aborder un problème et d’en concevoir la solution.
-   Quelques paradigmes
    -   Programmation impérative
        -   Programmation structurée
        -   Programmation modulaire
        -   Programmation par abstraction de données
        -   Programmation objet
    -   Programmation fonctionnelle
    -   Programmation logique
-   Un langage **supporte un paradigme** quand il fournit les fonctionnalités pour utiliser ce style (de façon simple, sécurisée et efficace)

### Exemple - Programmation logique avec Prolog
-   Prolog permet de définir et d’interroger une *base de faits*
-   Prolog est un langage déclaratif
-   Un *fait* est une assertion simple
```prolog
- Idéfix est un chien
chien(idefix).
```

-   Une *règle* décrit une inférence à partir des faits
```prolog
- Les chiens aiment les arbres
aimeLesArbres(X):- chien(X).
```

-   Une *requête* est une question sur la *base de connaissance*
```prolog
- Idéfix aime-t'il les arbres ?
?- aimeLesArbres(idefix)
```

### Solveur de Sudoku 4*x**x*4 en Prolog - Requête
```prolog
- requête
| ?- sudoku([_, _, 2, 3,
             _, _, _, _,
             _, _, _, _,
             3, 4, _, _],
             Solution).
```

### Solveur de Sudoku 4*x**x*4 en Prolog - Résolution 1/3
```prolog
- la solution doit être unifiée avec le problème
- le problème comporte 16 chiffres
- chaque chiffre est compris entre 1 et 4 (fd_domain)

sudoku(Puzzle, Solution) :-
  Solution = Puzzle,
  Puzzle = [A1, A2, A3, A4,
            B1, B2, B3, B4,
            C1, C2, C3, C4,
            D1, D2, D3, D4],
  fd_domain(Puzzle, 1, 4),
```

### Solveur de Sudoku 4*x**x*4 en Prolog - Résolution 2/3
```prolog
- les blocs (lignes, colonnes et carrés) sont définis

Row1 = [A1, A2, A3, A4],
Row2 = [B1, B2, B3, B4],
Row3 = [C1, C2, C3, C4],
Row4 = [D1, D2, D3, D4],

Col1 = [A1, B1, C1, D1],
Col2 = [A2, B2, C2, D2],
Col3 = [A3, B3, C3, D3],
Col4 = [A4, B4, C4, D4],

Square1 = [A1, A2, B1, B2],
Square2 = [A3, A4, B3, B4],
Square3 = [C1, C2, D1, D2],
Square4 = [C3, C4, D3, D4],
```

### Solveur de Sudoku 4*x**x*4 en Prolog - Résolution 3/3
```prolog
- le prédicat valid reçoit une liste de 12 blocs
- la liste vide est valide
- la tête de la liste ne comporte pas de doublons (fd_all_different)
- le reste de la liste doit être valide

valid([]).
valid([Head|Tail]) :-
  fd_all_different(Head),
  valid(Tail).

- une solution possède des blocs valides

valid([Row1, Row2, Row3, Row4,
        Col1, Col2, Col3, Col4,
        Square1, Square2, Square3, Square4]).
```

### Exemple - Programmation fonctionnelle avec Haskell
-   Haskell est un langage fonctionnel
-   Possède un système de typage statique, fort et principalement implicite (inférence de types)

### Haskell 1/2
```haskell
-- Calcul de la fonction factorielle

-- Récursive
fact x = if x == 0 then 1 else fact (x - 1) * x

-- Pattern matching
fact 0 = 1
fact x = x * fact (x - 1)

-- Gardes
fact x
   | x > 1 = x * fact (x - 1)
   | otherwise = 1

-- Liste et intervalle
fac x = product [1..x]
```

### Haskell 2/2
===========
```haskell
-- Fonctions d'ordre supérieure
mapList f [] = []
mapList f (x:xs) = f x : mapList f xs

-- Listes en compréhension et évaluation paresseuse
take 10 [ (i,j) | i <- [1..], j <- [1..], i < j ]
```

### Langage impératif
-   Un *langage impératif* représente un programme comme une séquence d’instructions qui modifient son état au cours de son exécution
-   Un programme décrit **comment** aboutir à la solution du problème
-   Proche de l’architecture matérielle des ordinateurs (*architecture de von Neumann*)
-   De nombreux langages populaires sont de ce type (C, Java, Python)

### Langage déclaratif
-   Un *langage déclaratif* permet de décrire ce que le programme doit faire (le **quoi**) et non pas comment il doit le faire (le **comment**)
-   Un programme respectant ce style décrit le problème à traiter
-   Quelques exemples : Prolog, SQL
-   Certains langages impératifs embarquent des constructions déclaratives

## Gestion de la mémoire
-   La gestion de la mémoire dans un langage de programmation définit le modèle mémoire utilisé par le langage
-   Elle décrit également comment les objets inutilisés sont identifiés et désalloués
    -   nécessaire pour éviter les *fuites de mémoire* (*memory leaks*)
-   La plupart des langages ont une gestion automatique de la mémoire et s’appuient sur un *ramasse-miettes* (*garbage collector*)

**En Java, le ramasse-miettes est chargé de libérer la mémoire allouée dynamiquement.**
```java
int[] tableau = new int[10]; // allocation d'un tableau de 10 cases
// la désallocation est automatique
```
-   Les langages C et C++ ont une gestion manuelle de la mémoire
```c
int[] tableau = malloc(10 * sizeof(int)); // allocation d'un tableau de 10 cases
// ...
free(tableau); // libération de la mémoire
```

## Caractéristiques de quelques langages

| Langage | Implémentation | Scripts | Typage | Paradigme | Mémoire |
|---|---|---|---|---|---|
| C | Compilé | Non | explicite, statique | procédural | manuelle
| Java | Compilé, interprété | Non | explicite, statique | OO, fonc., générique | auto
| PHP | Interprété | Oui | implicite, dynamique | proc., OO | auto
| Python | Compilé, Interprété | Oui | implicite, dynamique | proc., OO, fonc. | auto
| Scala | Compilé, interprété | Oui | implicite, statique | OO, fonc., générique | auto
