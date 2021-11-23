#hangman game
import random,requests


def select_game():
    select=input("Welcome to Hangman, do you want to Enter(E) a word or have it selected at Random(R): ")
    if select=='e':
        word_enter()
    elif select=='r':
        random_word()
    else:
        print("Please enter \'r\' or \'e\'")
        select_game()
        

def random_word():
    #return random word 
    word_site="https://www.mit.edu/~ecprice/wordlist.10000"

    response=requests.get(word_site)
    WORDS=response.content.splitlines()
    wordIndex=random.randint(0,len(WORDS)-1)
    n_word=str(WORDS[wordIndex]).split("b'")[1].split("'")[0]

    word_guess(n_word)


def word_enter():
    word=''
    bad_char={"/",".",",","[","]",")","(","&","%"}
    bad_key="False"
    word=input("Enter your word or phrase: ")
    for i in word:
        if i in bad_char:
            bad_key="True"

    if word == "" or bad_key=="True":   
        print("Word is invalid: ")
        word_enter()
    else:
        word_guess(word)

def word_guess(word):
    global chance
    global correct

    word_array=[]
    temp_array=[]
    incorrect=[]
    word_len=len(word)
    fill_array=[]
    answer_word=''
    for i in range(0,word_len):
        fill_array.append('_')
        answer_word=answer_word+fill_array[i]
    for j in word:
        word_array.append(j)
    
    temp_array=word_array

    while chance!=0:
        guess=input(f"Word: {answer_word} Incorrect Letter: {incorrect} Remainding Chances: {chance} Guess: ")
        if guess in word_array:             #guess is correct
            fill_array,answer_word,correct=word_fill(temp_array, fill_array,guess,correct)      #calls word_fill, returns answer word and fill array 
            word_array=remove(word_array,guess)                                 #calls remove which retums word_array minus guess letter
            if correct == word_len:
                print("correct you have completed the game")
        #guess is incorrect
        else:
            incorrect.append(guess)
            chance-=1
            hangman_pic(chance,word)
            
        
           
"""
            place=guess[index]
            correct+=1
            word_array.pop(guess)
            print(word_array)
            #print(f"True {guess} count {correct}")

        else:
            incorrect.append(guess)
            chance-=1
            print(f"false: {incorrect} chance {chance}")
   

    #for i in word:
        #if guess==i:
            #correct+=1
            #print("The letter "+ guess+" is correct "+correct)
        #else:
            #print("false")
"""

def remove(word_array,guess):
    return [value for value in word_array if value !=guess]


def word_fill(temp_array, fill_array,guess,correct):
    answer_word=''
    for i,val in enumerate(temp_array):
        if val ==guess:
            fill_array[i]=guess
            correct+=1
        answer_word=answer_word+fill_array[i]

    return fill_array,answer_word,correct

def hangman_pic(chance,word):
    if chance==5:
        print(" +------+")
        print(" |      |")
        print(" |      o")
        print(" |")
        print(" |")
        print(" |")
        print("====")
    elif chance ==4:
        print(" +------+")
        print(" |      |")
        print(" |      o")
        print(" |      |")
        print(" |")
        print(" |")
        print("====")
    elif chance==3:
        print(" +------+")
        print(" |      |")
        print(" |      o")
        print(" |     /|")
        print(" |")
        print(" |")
        print("====")
    elif chance ==2:
        print(" +------+")
        print(" |      |")
        print(" |      o")
        print(" |     /|\\")
        print(" |")
        print(" |")
        print("====")
    elif chance==1:
        print(" +------+")
        print(" |      |")
        print(" |      o")
        print(" |     /|\\")
        print(" |     /")
        print(" |")
        print("====")
    else:
        print(" +------+")
        print(" |      |")
        print(" |      o")
        print(" |     /|\\")
        print(" |     / \\")
        print(" |")
        print("====")
        new_game=input("Game over: the word was \""+word+"\", dumbass!! Do you want to play again \"Yes\" or \"No\"").lower
        if  new_game=='yes' or 'y':
            word_enter()
        else:
            exit()

if __name__=="__main__":
    chance=6
    correct=0
    select_game()