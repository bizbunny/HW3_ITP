>>> from hw3 import *

##### Problem 1 #####
Write a function cheer that takes as a parameter a mascot string and PRINTS out the following cheer for input 'mascot':
"""
How do you spell winner?
I know, I know!
M A S C O T !
And that's how you spell winner!
Go Mascot!
"""
(Note the format of all caps with spaces in the middle line and capitalized on the last line)

>>> cheer('Huskies')
How do you spell winner?
I know, I know!
H U S K I E S !
And that's how you spell winner!
Go Huskies!
>>> cheer('BEARS')
How do you spell winner?
I know, I know!
B E A R S !
And that's how you spell winner!
Go Bears!
>>> cheer('koalas')
How do you spell winner?
I know, I know!
K O A L A S !
And that's how you spell winner!
Go Koalas!


##### Problem 2 #####
Write a function vowelCount that takes as a parameter a string of text and PRINTS out the following response for input 'AeIoU':
"""
a, e, i, o, and u appear, repsectively, 1, 1, 1, 1, 1 times.
"""
(Note this includes capital letters)

>>> vowelCount('The quick red fox jumped over the lazy brown dog.')
a, e, i, o, and u appear, respectively, 1, 5, 1, 4, 2 times.
>>> vowelCount('AeIoU')
a, e, i, o, and u appear, respectively, 1, 1, 1, 1, 1 times.
>>> vowelCount('Alabama')
a, e, i, o, and u appear, respectively, 4, 0, 0, 0, 0 times.


##### Problem 3 ######
Write a function hasDuplicate that takes as a parameter a file name and RETURNS True if the text file's FIRST LINE has duplicate words in it, or False otherwise:
To test this out, create a file "duplicates.txt" in the same folder as your hw3.py file with duplicates words, e.g.
"""
This duplicates file has duplicates in its text
"""
And create a file "noDuplicates.txt" in the same folder with no duplicate words, e.g.
"""
This file has no duplicates in its text
"""

>>> hasDuplicate('duplicates.txt')
True
>>> hasDuplicate('duplicates.txt')==True
True
>>> hasDuplicate('noDuplicates.txt')
False
>>> hasDuplicate('noDuplicates.txt')==False
True



NOTE: Problems 4 and 5 will use a comma-separated value (csv) file "cubsRoster.csv". Download it from D2L and place it into the same folder as hw3.py
You can expect it will have schema
"""
Name,Age,CountryCode,
Anthony Rizzo,29,US,
...
Yu Darvish,32,JP,
...
Rowan Wick,26,CA,
"""
Note the string split method will be helpful for turning each line into an array which has as elements player name, age and country code.


##### Problem 4 ######
Write a function printWithAge that takes as parameters a file name and an age and prints out the name of each player that is that age:

>>> printWithAge('cubsRoster.csv', 35)
Tony Barnette
Cole Hamels
Jon Lester
>>> printWithAge('cubsRoster.csv', 24)
Adbert Alzolay
Ian Happ
Duane Underwood Jr.
>>> printWithAge('cubsRoster.csv', 31)
Craig Kimbrel
>>> printWithAge('cubsRoster.csv', 38)
Ben Zobrist



##### Problem 5 ######
Write a function printWithCountryCode that takes as parameters a file name and a country code and prints out the name of each player with that country code

>>> printWithCountryCode('cubsRoster.csv', 'DO')
Robel Garcia
Randy Rosario
Pedro Strop
>>> printWithCountryCode('cubsRoster.csv', 'JP')
Yu Darvish
>>> printWithCountryCode('cubsRoster.csv', 'PR')
Javier Baez
Victor Caratini
Xavier Cedeno
Martin Maldonado
>>> printWithCountryCode('cubsRoster.csv', 'CA')
Jim Adduci
Rowan Wick