#hangman game

def word_enter():
    bad_char={"/",".",",","[","]",")","(","&","%"}
    word=input("Enter your word or phrase: ")
    if word != "":
        for i in bad_char:
            if i not in word:
                continue
            else:
                word_enter()   
        word_guess(word)
    #print("Word entered is invalid.")
    #word_enter()

def word_guess(word):
    print(f"the word entered is {word}")







if __name__=="__main__":
    word_enter()