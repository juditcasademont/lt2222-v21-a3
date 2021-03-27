# LT2222 V21 Assignment 3

Your name: Judit Casademont Moner (guscasaju)

## Part 1
*Function a*
Function a takes a file and returns a list of strings which are the characters (letters or spaces) in the text file and a set of said strings (unique instances of the characters).
It first opens the file as q, then it loops for l (line) in q (the file) and it adds to mm (the list of characters) all characters (c for c in l). Finally, it adds two start tokens at the start of the list and two end tokens at the end of the list. 

*Function g*
Function g returns an array of the length of p and with as many indexes as x, filled with character counts. It takes x and p, x is a 4-element list containing four characters and p is the set of unique characters we obtained from function a.
It first creates a matrix full of 0s and fills it with the counts of the characters in x.

*Function b*
Function b builds two arrays (gr and gt), gr is an array containing the features/context characters (2 letters before and 2 letters after each vowel) and gt is an array containing the indexes of the vowels in the document (so, the position where vowels are found).
It takes u, which is the list of characters returned by function a, and p, the set also returned by function a. It loops over u and, for every index, it checks if it's a vowel. If it's not a vowel, it keeps checking, but whenever it finds a vowel it stores its index in gt and it stores the array resulting of passing the two characters previous to the vowel and the two characters after through function g, and stores it in gr.

*Arguments*
The "--k" argument refers to the hidden layer.
The "--r" argument determines the number of epochs.
The "m" argument refers to the input file.
The "h" argument refers to the output file.

## Part 2

## Part 3

| Tables   |      Are      |  Cool |
|----------|:-------------:|------:|
| col 1 is |  left-aligned | $1600 |
| col 2 is |    centered   |   $12 |
| col 3 is | right-aligned |    $1 |

| Model name | r parameter | k parameter | accuracy |
| :---: | :---: | :---: | :---: | :---: |
| model_rdefault_k100 | 100 | 100 | 31% |
| model_rdefault_k250 | 100 | 250 | 40% |
| model_rdefault_k300 | 100 | 300 | 46% |
| model_rdefault_k350 | 100 | 350 | 30% |
| model_rdefault_k400 | 100 | 400 | 13% |

## Bonuses

## Other notes
