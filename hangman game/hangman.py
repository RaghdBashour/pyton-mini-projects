
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    counter=0
    for i in range(len(letters_guessed)):  
        for j in range(len(secret_word)):
            if(secret_word[j]== letters_guessed[i]):
                counter +=1
            
    if(counter >= len(secret_word)):
        return True
    else:
        return False
    
    
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    new_word=''
    for i in range(len(secret_word)):  
        for j in range(len(letters_guessed)):
            if(secret_word[i] == letters_guessed[j]):
                new_word += secret_word[i]
                break
            elif (j+1 == len(letters_guessed)):
                new_word += '_ '
        
                                                
            
    return new_word




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = ''
    for i in range(len(string.ascii_lowercase)):
        for j in range(len(letters_guessed)):
            if string.ascii_lowercase[i] == letters_guessed[j]:
                break
            elif(j == len(letters_guessed)-1):
                available_letters += string.ascii_lowercase[i]
        
    return available_letters
            
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    gusess = 6
    letters_guessed =[]
    new_word='_ '* len(secret_word)
    print('--------------------------')
    print('Welcome to the game Hangman! ')
    print('i am thinking of a word that is ',len(secret_word),'letters long.')
    print('--------------------------')
    print('you have gusess',gusess,' left')
    print('available letters: ',string.ascii_lowercase)
    print('--------------------------')
    
    while is_word_guessed(secret_word, letters_guessed)==False:
        if(gusess == 0):
            break;
        letters_guessed += input('enter your guess: ')                
        result =get_guessed_word(secret_word, letters_guessed)
        if(result != new_word):
            new_word = result
            print('good guess:',result)
            print('available letters: ',get_available_letters(letters_guessed))
            print('--------------------------')
        else:
            gusess -=1
            print('oops! bad guess now you have',gusess,'guesses')
            print('available letters: ',get_available_letters(letters_guessed))
            print('your word:',result)
            print('--------------------------')

    if(is_word_guessed(secret_word, letters_guessed) == False):
        print('**************************')
        print('Game Over! ＞︿＜')
        print('**************************')
    elif(is_word_guessed(secret_word, letters_guessed)== True):
        print('**************************')
        print('You Won! ㄟ(≧◇≦)ㄏ')
        print('**************************')        




def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    '''
    take the parameters clean them compare length if all good
    check for the _ symbol if its thier we will look for any duplicate letters 
    in the other wordd in the same index of the _ if also all good
    we will countinue to the letters that are not _ and add them to the lists then 
    compare lists if equal it True a possible solution if anything fails in the procces 
    it return False as it cant be a solution
    
    '''
    my_word = my_word.replace(' ','')
             
    new_word=[]
    compare_word=[]
    count=0
    if(len(my_word)!= len(other_word)):
        return False
    for my_char , other_char in zip(my_word,other_word):
        if(my_char == '_'):
            for char in other_word:
                if(char==other_char and other_char in my_word):
                    count+=1
                if(count>1):
                    return False
        else:
            new_word.append(my_char)
            compare_word.append(other_char)
        

    if(new_word == compare_word):
        return True
    else:
        return  False
                    
            
                


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matches =[]
    for word in wordlist:
        if(match_with_gaps(my_word,word) == True):
            possible_matches.append(word)
    
    if(len(possible_matches)==0):
        print('No matches found ')

    else:
        print(' '.join(possible_matches))
            
    


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    gusess = 6
    letters_guessed =[]
    new_word='_ '* len(secret_word)
    print('--------------------------')
    print('Welcome to the game Hangman! ')
    print('i am thinking of a word that is ',len(secret_word),'letters long.')
    print('--------------------------')
    print('you have ',gusess,'gusess left')
    print('available letters: ',string.ascii_lowercase)
    print('--------------------------')
    
    while is_word_guessed(secret_word, letters_guessed)==False:
        if(gusess == 0):
            break;
        letters_guessed += input('enter your guess: ')                
        result =get_guessed_word(secret_word, letters_guessed)
        if(result != new_word):
            new_word = result
            print('good guess:',result)
            print('you have ',gusess,'gusess left')
            print('available letters: ',get_available_letters(letters_guessed))
            print('--------------------------')
        else:
            if(letters_guessed[-1] =='*' and gusess == 1):
                show_possible_matches(result)
            elif(letters_guessed[-1] =='*' and gusess != 1):
                print('you can only use hints when you have 1 gusess')
            else:
                gusess -=1
                if(gusess == 1):
                    print('you can use hints now useing *')
                print('oops! bad guess now you have',gusess,'guesses')
                print('available letters: ',get_available_letters(letters_guessed))
                print('your word:',result)
            print('--------------------------')

    if(is_word_guessed(secret_word, letters_guessed) == False):
        print('**************************')
        print('Game Over! ＞︿＜')
        print('**************************')
    elif(is_word_guessed(secret_word, letters_guessed)== True):
        print('**************************')
        print('You Won! ㄟ(≧◇≦)ㄏ')
        print('**************************')  
    



if __name__ == "__main__":

    #hangman without hints
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

    #hangman with hints
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
