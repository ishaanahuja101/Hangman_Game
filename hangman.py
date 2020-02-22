import string

def isWordGuessed(secretWord, lettersGuessed):
    count = 0
    for i, c in enumerate(secretWord):
    	if c in lettersGuessed:
    		count += 1
    if count == len(secretWord):
    	return True
    else:
    	return False


def getGuessedWord(secretWord, lettersGuessed):
    count = 0
    blank = ['_ '] * len(secretWord)

    for i, c in enumerate(secretWord):
        if c in lettersGuessed:
            count += 1
            blank.insert(count-1,c)
            blank.pop(count)
            if count == len(secretWord):
                return ''.join(str(e) for e in blank)
        else:
            count += 1
            blank.insert(count-1,'_')
            blank.pop(count)
            if count == len(secretWord):
                return ''.join(str(e) for e in blank)
        
def getAvailableLetters(lettersGuessed):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet2 = alphabet[:]

    def removeDupsBetter(L1, L2):
        L1Start = L1[:]
        for e in L1:
            if e in L1Start:
                L2.remove(e)
        return ''.join(str(e) for e in L2)

    return removeDupsBetter(lettersGuessed, alphabet2)


            
    

def hangman(secretWord):
    intro = str(len(secretWord))
    lettersGuessed = []
    guess = str
    mistakesMade = 8
    wordGuessed = False
    
    print 'Welcome to the game, Hangman!'
    print ('I am thinking of a word that is ') + intro + (' letters long.')
    print ('------------')

    while mistakesMade > 0 and mistakesMade <= 8 and wordGuessed is False:
        if secretWord == getGuessedWord(secretWord, lettersGuessed):
            wordGuessed = True
            break
        print ('You have ') + str(mistakesMade) + (' guesses left.')
        print ('Available letters: ') + getAvailableLetters(lettersGuessed)
        guess = raw_input('Please guess a letter: ').lower()
        if guess in secretWord:
            if guess in lettersGuessed:
                print ("Oops! You've already guessed that letter: ") + getGuessedWord(secretWord, lettersGuessed)
                print ('------------')
            else:
                lettersGuessed.append(guess)
                print ('Good guess: ') + getGuessedWord(secretWord, lettersGuessed)
                print ('------------')
        else:
            if guess in lettersGuessed:
                print ("Oops! You've already guessed that letter: ") + getGuessedWord(secretWord, lettersGuessed)
                print ('------------')
            else:
                lettersGuessed.append(guess)
                mistakesMade -= 1
                print ('Oops! That letter is not in my word: ') + getGuessedWord(secretWord, lettersGuessed)
                print ('------------')

    if wordGuessed == True:
        return 'Congratulations, you won!'
    elif mistakesMade == 0:
        print ('Sorry, you ran out of guesses. The word was ') + secretWord

hangman(input().lower())
