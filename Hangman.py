inputWord = list(input('Enter the word: '))
wordSize = len(inputWord)
gameStatus = True
noOfChance = 5
letterCmp = False
checkWord = []
for i in range(wordSize):
    checkWord.append('_')

while gameStatus:
    print(checkWord)
    checkLetter = input('Enter the letter: ')

    for i in range(wordSize):
        if checkLetter == inputWord[i]:
            checkWord[i] = checkLetter
            letterCmp = True

    if letterCmp:
        if inputWord == checkWord:
            print(checkWord,'\nFound it')
            gameStatus = False
        letterCmp = False
    else:
        noOfChance -= 1
        print('Life lost, remaining',noOfChance)
        if noOfChance == 0:
            print('You Lost')
            gameStatus = False



