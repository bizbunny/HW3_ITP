#Collaborator: Linh Nguyen
import csv
##### Problem 1 #####
#Answer
def cheer(mascot):
	print('How do you spell winner?')
	print('I know, I know!')
	mC=mascot.upper()
	mCap=mascot.capitalize()
	for mL in list(mC):
		print(mL, end=' ')
	print('!\nAnd that\'s how you spell winner!')
	print('Go '+mCap+'!')
##### Problem 2 #####
#Answer
def vowelCount(vowelV):
    vowelV = vowelV.lower()
    vowelCheck = list('aeiou')
    aN = 0
    eN = 0
    iN = 0
    oN = 0
    uN = 0
    for vL in vowelV:
        if(vL in vowelCheck and vL == 'a'):
            aN += 1
        if (vL in vowelCheck and vL == 'e'):
            eN += 1
        if (vL in vowelCheck and vL == 'i'):
            iN += 1
        if (vL in vowelCheck and vL == 'o'):
            oN += 1
        if (vL in vowelCheck and vL == 'u'):
            uN += 1
    print('a, e, i, o, and u appear, respectively, ' + str(aN) + ', ' + str(eN) + ', ' + str(iN) + ', ' + str(oN) + ', ' + str(uN) + ' times.')
##### Problem 3 ######
#Answer
def hasDuplicate(fILe):
    text = open(fILe, 'r')
    text = text.read()
    text = text.replace(',', '')
    text = text.replace('.', '')
    text = text.replace('?', '')
    text = text.replace('\'','')
    words = text.split()
    counts = {}
    for word in words:
        if word not in counts:
            counts[word] = 0
        counts[word] += 1

    for i in counts:
        if(int(counts[i]) > 1):
            return True
    return False
##### Problem 4 ######
#Answer
def printWithAge(file_name, age):
    with open(file_name, 'r') as fiLe:
        header = next(fiLe)
        reader = csv.reader(fiLe, delimiter=',')
        for i in reader:
            if (int(i[1]) == int(age)):
                print(i[0])
##### Problem 5 ######
#Answer
def printWithCountryCode(file_name, Countrycode):
    with open(file_name, 'r') as fiLe:
        header = next(fiLe)
        countryDict={'US': 'United States','CA':'Canada','VE':'Venezuela','PR':'Puerto Rico','JP':'Japan','DO':'Dominican Republic','CO':'Colombia'}
        reader = csv.reader(fiLe, delimiter=',')
        for i in reader:
            if (i[2] == Countrycode and countryDict.keys):
                print(i[0])
if __name__=='__main__':

   import doctest

   print(doctest.testfile('hw3_test.py', verbose=True))
