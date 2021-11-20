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
    global chance
    global correct

    word_array=[]
    incorrect=[]
    #chance=0
    #correct=0
    word_len=len(word)
    
    for j in word:
        word_array.append(j)

    while chance <= 5:
        guess=input(print("Guess a letter: "))
        if guess in word_array:
            word_array=remove(word_array,guess)
            
"""
            place=guess[index]
            correct+=1
            word_array.pop(guess)
            print(word_array)
            #print(f"True {guess} count {correct}")

        else:
            incorrect.append(guess)
            chance+=1
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







if __name__=="__main__":
    chance=0
    correct=0
    word_enter()