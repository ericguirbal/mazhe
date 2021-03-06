# Erratum du Frido

Ce fichier contient les fautes découvertes dans les versions imprimées du Frido. Elles sont en principe corrigées au fur et à mesure dans la [version courante](http://laurent.claessens-donadello.eu/pdf/lefrido.pdf).

## Frido 2017

Les fautes sont présentées par ordre anti-chronoligique de découvertes.

- Volume 2. La définition de mesure positive sur un espace mesurable est incorrecte (définition 13.23). La première condition doit être remplacée par 
        mu(vide)=0.
    Sinon, il est possible d'avoir une mesure pour laquelle tous les éléments de la tribu ont une mesure infinie (y compris le vide). Dans
    ce cas, la remarque qui suit la définition de la mesure ne s'applique pas (remarque 13.24), et il n'est en réalité pas garanti d'avoir mu(vide)=0.

- Volumes 1 et 2. Définition de la limite. Induit en erreur à moitié par mon manque d'attention et à moitié par Wikipédia, la définition de la limite d'une fonction était incorrecte, et surtout incohérente avec les théorèmes démontrés plus bas.

    La définition correcte de la limite se fait *en excluant* le point vers lesquel on fait tendre x.

- Volume 1. Définition 4.8. La définition du pgcd dans un anneau n'est pas correcte. 'd' est un pgcd de 'a' et 'b' si tout diviseur commun de 'a' et 'b' divise 'd' ET SI 'd' divise 'a' et 'b'.

- Volume 3. Définition 24.63. La définition d'espace réflexif n'est pas correcte; il faut parler de bidual. Du coup l'énoncé du théorème 24.64 (qui est probablement bien vrai quand même) est à prendre avec des précautions.

- Volume 1. Proposition 4.70. Je suis presque certain qu'il faut ajouter l'hypothèse que I est un idéal propre, c'est à dire que l'inclusion de I dans A est stricte.

- Volume 1. L'exemple 4.73 prétend que les anneaux Z/nZ sont principaux. Cela n'est pas vrai en général parce que lorsque `n` n'est pas premier, Z/nZ n'est pas intègre. Il est tout de même vrai que ses idéaux sont principaux.

- Volume 1. L'exemple 4.85 prétend que Z n'est ni principal ni euclidien. En réalité, Z est euclidien (et donc principal) parce que la valeur absolue donne un stathme. [merci cdr](https://github.com/LaurentClaessens/mazhe/issues/58).

