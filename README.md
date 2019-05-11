# Lista 4 
## Alunos:
Lucas Siqueira - 15/0137567

Lucas Macedo - 15/0137397

## Descrição:

Consiste na entrada de palavras separadas por um unico espaço, em que a partir da utilização do radix sort são ordendas, em seguida as palavras são agrupadas em uma unica string, com essa string ordenamos as letras pela frequencia em que elas aparecem, posteriormente utilizando heap fazemos um rearranjo dos caracteres de modo que não haja dois adjacentes iguais. 

## Para executar:

> python3 main.py

**Entre com palavras separadas por um unico espaço**

Input: aaa bc 

Output: 

> Ordenando alfabeticamente atraves do radix sort ->

> ['aaa', 'bc.', '...']

> ['aaa', 'bc.', '...']

> ['aaa', 'bc.', '...']

> ['aaa', 'bc.', '...']

> ['aaa', 'bc', '']

> Transformando as palavras ordenadas em uma grande palavra ->

> aaabc

> Ordenando decrescentemente pela frequencia das letras utilizando heap sort ->

> aaacb

> Transformando as palavras ordenadas em uma grande palavra ->

> aaabc

> Rearanjando letras de forma que nao hajam letras iguais lado a lado ->

> [['a', 3], ['c', 1], ['b', 1]]

> [['b', 1], ['c', 1]]

> [['a', 2], ['c', 1]]

> [['c', 1]]

> [['a', 1]]

> abaca

Input: aa bc aa 

Output:

> Ordenando alfabeticamente atraves do radix sort ->

> ['aa', 'bc', 'aa']

> ['aa', 'aa', 'bc']

>['aa', 'aa', 'bc']

>['aa', 'aa', 'bc']

>Transformando as palavras ordenadas em uma grande palavra ->

>aabcaa

>Ordenando decrescentemente pela frequencia das letras utilizando heap sort ->

>aaaacb

>Transformando as palavras ordenadas em uma grande palavra ->

>aabcaa

> Rearanjando letras de forma que nao hajam letras iguais lado a lado ->

>[['a', 4], ['c', 1], ['b', 1]]

>[['b', 1], ['c', 1]]

>[['a', 3], ['c', 1]]

>[['c', 1]]

>[['a', 2]]

>Deu ruim parça!

## Referências
>https://www.quora.com/How-can-I-sort-strings-using-Radix-Sort

>https://www.geeksforgeeks.org/rearrange-characters-string-no-two-adjacent/
