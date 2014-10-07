import WordMemory

def doAddWords():
    while(True):
        Word = input("Please enter a word to process or enter \"/q\" to quit: ")
        print("\n")
 
        if(   Word == '/q' ):
            break
        
        elif( Word == "" ):
            print("Disregarding blank character...\n")
        
        else:
            choice = input("The word \"{0}\" is going to be added to the WordMemory, are you sure? (N for NO, anything else for YES): ".format(Word))
            
            if( choice == "N" ):
                print("Okay, disregarding that word.")
                
            else:
                WordMemory.addWord(Word)
                print("\nThank you, your word \"{0}\" has been processed.\n".format(Word))