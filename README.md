# LT2222 V21 Assignment 3

Your name: Judit Casademont Moner (guscasaju)

## Part 1
### Function a
Function a takes a file and returns a list of strings which are the characters (letters or spaces) in the text file and a set of said strings (unique instances of the characters).
It first opens the file as q, then it loops for l (line) in q (the file) and it adds to mm (the list of characters) all characters (c for c in l). Finally, it adds two start tokens at the start of the list and two end tokens at the end of the list. 

### Function g
Function g returns an array of the length of p and with as many indexes as x, filled with character counts. It takes x and p, x is a 4-element list containing four characters and p is the set of unique characters we obtained from function a.
It first creates a matrix full of 0s and fills it with the counts of the characters in x.

### Function b
Function b builds two arrays (gr and gt), gr is an array containing the features/context characters (2 letters before and 2 letters after each vowel) and gt is an array containing the indexes of the vowels in the document (so, the position where vowels are found).
It takes u, which is the list of characters returned by function a, and p, the set also returned by function a. It loops over u and, for every index, it checks if it's a vowel. If it's not a vowel, it keeps checking, but whenever it finds a vowel it stores its index in gt and it stores the array resulting of passing the two characters previous to the vowel and the two characters after through function g, and stores it in gr.

### Arguments
The "--k" argument refers to the hidden layer.
The "--r" argument determines the number of epochs.
The "m" argument refers to the input file.
The "h" argument refers to the output file.

## Part 2

I worked on this code in close collaboration with Sigrid Jonsson and Sarab Youssef. As a consequence, our codes will likely be similar.

## Part 3

The following are my results of training and evaluating the models

| Model name | r parameter | k parameter | Accuracy |
| :--------: | :---------: | :---------: | :------: |
| model_bothdefault | 100 | 200 | 42% |
| model_rdefault_k100 | 100 | 100 | 31% |
| model_rdefault_k250 | 100 | 250 | 40% |
| model_rdefault_k300 | 100 | 300 | 46% |
| model_rdefault_k350 | 100 | 350 | 30% |
| model_rdefault_k400 | 100 | 400 | 13% |
| model_kdefault_r50 | 50 | 200 | 38% |
| model_kdefault_r150 | 150 | 200 | 24% |
| model_kdefault_r200 | 200 | 200 | 17% |
| model_kdefault_r300 | 300 | 200 | 9% |
| model_kdefault_r400 | 400 | 200 | 10% |

The model that gave me the highest accuracy rate, at 46%, was the one with the parameter r (number of epochs) was set to a default 100 and the parameter k (hidden layer) was set to 300.

As for patterns in the accuracy results, I would say that the best results are obtained at the default number of epochs (100) at around 200 to 300 hidden layers, whereas the lowest ones usually occur when the hidden layer is set to its default (200) and the number of epochs grow over 150 or 200, as well with 400 hidden layers and the default number of epochs. It seems like the logic of "the higher the number of hidden layers and epochs the better the results will be" is not applicable in this case. By seeing this data, I come up with the hypothesis that, with higher numbers, the model might suffer from overfitting. Said in other words, it might be that the model gets trained so much that it learns the training data so well that it worsens the performance when encountered with data that hasn't yet been seen.

When taking a look at the output file, the most noticeable thing is that the words that were guessed correctly more often were the ones with only one vowel in them, especially conjunctions, subjunctions, prepositions and pronouns, such as: *och, att, för, som, min, den, till, på, han, om*, etc. Other words that are generally guessed correctly are common use verbs, for example: *komma, göra, åka, ha, kunna, bli*, etc. My deduction when seeing this output is that the more common a word is, the more exposure the model gets to it. Therefore, the easier it gets for the model to predict it correctly.

Short collection of words I randomly found in my output file that were guessed wrong and I find funny, because why not:
- öpsala (should be Upsala - old version of current Uppsala)
- hjölp (should be hjälp - help)
- ſammarbåté (should be ſamarbete - old version of current samarbete, collaboration - with the é it makes me think of some fancy French word)
- åribri (should be Örebro)
- mindigen (should be måndagen - Monday - makes Monday look cute)

## Bonuses

## Other notes
