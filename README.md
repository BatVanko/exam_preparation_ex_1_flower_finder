# exam_preparation_ex_1_flower_finder

You will be given two sequences of characters, representing vowels and consonants. Your task is to start checking if the following words could be found:
•	"rose"
•	"tulip"
•	"lotus"
•	"daffodil"
Start by taking the first character of the vowels collection and the last character from the consonants collection. Then check if these letters are present in one or more of the given words. If a letter is present, that part of the word is considered found. The word is gradually revealed with each letter found. Continue processing the next couple of letters until you find one of the given words above.
A letter (vowels or consonants) could participate in more than one word or more than one time in a word, for example:
•	The letter "o" is present in "rose", "lotus", and "daffodil". 
•	The letter "l" is present in "tulip", "lotus", and "daffodil".
•	The letter "f" is present in the word "daffodil" twice.
The consonant and the vowel are always removed from the collection after trying to match them with the letters in the given words (whether successful or not). In the end, the program stops when a word is found, or there are no more vowels or consonants.
As a result, if you found a word, print it and the remaining letters in each collection in the format described below. Otherwise, print "Cannot find any word!" on the first line and the remaining letters in each sequence in the format described below.

•	All letters will be lowercase.
•	The letter 'y' will always be a vowel.
•	The letter 'w' will always be a consonant.


Input
o e a o e a i
p r s x r

Output
Word found: rose
Vowels left: o e a i
Consonants left: p r
