# PushSwap Visualizer 🔄

Bienvenue dans le PushSwap Visualizer ! Si vous êtes curieux de voir comment fonctionne l'algorithme PushSwap avec différentes listes et souhaitez le visualiser en action, vous êtes au bon endroit. Vous n'avez pas besoin d'être un expert pour utiliser cet outil, il est conçu pour être simple et intuitif.

## Qu'es ce que le PushSwap ? 🤔

Le projet PushSwap est un algorithme de tri. L'idée principale est simple : on dispose de deux piles, initialement, une pile contient un certain nombre d'entiers dans un ordre quelconque et l'autre est vide. L'objectif est de trier la première pile avec le moins d'opérations possibles en utilisant la pile secondaire comme espace de travail.

Voici les opérations que vous pouvez utiliser pour manipuler et trier les piles :

1.  sa : échange les deux premiers éléments de la pile A (ne fait rien s'il y a moins de deux éléments).
2.  sb : échange les deux premiers éléments de la pile B (ne fait rien s'il y a moins de deux éléments).
3.  ss : effectue les opérations sa et sb en même temps.
4.  pa : prend le premier élément de la pile B et le place à la première position de la pile A.
5.  pb : prend le premier élément de la pile A et le place à la première position de la pile B.
6.  ra : fait une rotation vers le haut de la pile A (le premier élément devient le dernier).
7.  rb : fait une rotation vers le haut de la pile B.
8.  rr : effectue les opérations ra et rb en même temps.
9.  rra : fait une rotation vers le bas de la pile A (le dernier élément devient le premier).
10. rrb : fait une rotation vers le bas de la pile B.
11. rrr : effectue les opérations rra et rrb en même temps.

## Comment l'utiliser ? 🚀

C'est simple:

python3 pushswap_bonus [instruction] list [flag]

**[instruction]**: C'est facultatif. Vous pouvez fournir les opérations du pushswap directement ou via un PIPE.
**list**: Votre liste d'entiers que vous souhaitez trier.
**[flag]**: Si vous utilisez `[-b]`, cela modifie légèrement la manière dont vous fournissez les entrées.
    *[-b]*: [instruction] -> path vers les opération | [list] -> path vers la liste d'entier
