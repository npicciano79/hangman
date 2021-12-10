#hangman game
import random,requests,time


def select_game():
    select=input("Welcome to Hangman, do you want to Enter(E) a word or have it selected at Random(R): ")
    if select.lower()=='e':
        word_enter()
    elif select.lower()=='r':
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
    answer_word=' '
    #creates blank word (answer_word) to be filled by correct guesses
    #creates filled, word_array, to match with guesses
    for i in range(0,word_len):
        fill_array.append('_')
        #input(f"fill array: {fill_array}")
        answer_word=answer_word+' '+fill_array[i]
        #input(f"answer word: {answer_word}")
    for j in word:
        word_array.append(j)
        #input(f"word array: {word_array}")
    temp_array=word_array

    while chance!=0:
        guess=input(f"Word: {answer_word} Incorrect Letter: {incorrect} Remaining Chances: {chance} Guess: ")
        if guess in word_array:             #guess is correct
            #fill_array,answer_word,correct=word_fill(guess,correct,temp_array,fill_array)  #     #calls word_fill, returns answer word and fill array 
            #word_array=remove(word_array,guess)                                 #calls remove which retums word_array minus guess letter
            correct+=1
            
            if correct>word_len/2:
                guess_the_word(word, fill_array)

            
            if correct == word_len:
                game_result=1
                end_game(game_result,word)

            
        #guess is incorrect
        else:
            incorrect.append(guess)
            chance-=1
            hangman_pic(chance,word)

def remove(word_array,guess):
    return [value for value in word_array if value !=guess]


def word_fill(guess,correct,temp_array,fill_array):           #temp_array, ,
    input(f"correct: {correct} guess{guess} temp array :{temp_array} fill array: {fill_array}")
    #answer_word=''
    for i,val in enumerate(temp_array):
        if val ==guess:
            fill_array[i]=guess
            correct+=1
        input(f"fill array: {fill_array}")
        #answer_word=answer_word+fill_array[i]

    #return fill_array,answer_word,correct

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
        game_result=0
        end_game(game_result,word)

def guess_the_word(word,fill_array):
    g_yesno=input("Would you like to guess the word \"Yes(Y)\" or \"No(N)\"?")
    if g_yesno.lower()=='yes' or 'y':
        y=input(" Enter your guess: ")
        if y==word:
            game_result=1
            end_game(game_result,word)
        else:
            print("Wrong Dumbass, keep guessing letters.")
            time.sleep(3)
            word_guess()





def end_game(game_result,word):
    if game_result==0:
        new_game=input("Game over: the word was \""+word+"\", dumbass!! Do you want to play again \"Yes(Y)\" or \"No(N)\"")
    else:
        new_game=input("Congratulations, you guesses "+word+" correctly.Do you want to play again \"Yes(Y)\" or \"No(N)\"")
    if  new_game.lower()=='yes' or 'y':
        select_game()
    else:
        exit()





if __name__=="__main__":
    chance=6
    correct=0
    select_game()