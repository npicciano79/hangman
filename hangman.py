#hangman game

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
    word_array=[]
    incorrect=[]
    chance=0
    correct=0
    word_len=len(word)
    
    for j in word:
        word_array.append(j)
    
    guess=input(print("Guess a letter: "))
   

    #for i in word:
        #if guess==i:
            #correct+=1
            #print("The letter "+ guess+" is correct "+correct)
        #else:
            #print("false")


    







if __name__=="__main__":
    word_enter()