import LetterLinkMemory

def doAddWords():
    while(True):
        String = input("Please enter a word, list of space separated words to process or enter \"/q\" to quit: ")
        print("\n")
 
        if(   String == '/q' ):
            break
        
        elif( String == "" ):
            print("Disregarding blank character...\n")
        
        else:
            Words = String.split(' ')
            
            for Word in Words:
                Choice = input("The word \"{0}\" is going to be added to the LetterLinkMemory, are you sure? (N for NO, anything else for YES): ".format(Word))
                
                if( Choice == "N" ):
                    print("Okay, disregarding that word.")
                    
                else:
                    LetterLinkMemory.addWord(Word)
                    print("\nThank you, your word \"{0}\" has been processed.\n".format(Word))
                
def doScanString():
    while(True):
        String = input("Please enter a string to process or enter \"/q\" to quit: ")
        print("\n")
        
        if(   String == '/q' ):
            break
        
        elif( String == "" ):
            print("Disregarding blank input...\n")
        
        else:
            Choice = input(
                """
                The string: \n\"{0}\"\nis going to be added to be scanned then added to the LetterLinkMemory, are you sure? 
                (N for NO, anything else for YES):
                """.format(String))
            
            if( Choice == "N" ):
                print("Okay, disregarding this string.")
                
            else:
                Words = LetterLinkMemory.scanForWords(String)
                print("\nThank you, your string \n\"{0}\"\n has been processed.\n".format(String))
                print("These are the words that have been picked up by the algorithm: \n{0}\n".format(", ".join(Words)))
                
                print("Now the algorithm will ask you to aid it in evaluating the words chosen.\n")
                
                for Word in Words:
                    
                    Choice = input("Is \"{0}\" a word (doesn't have to be a real word)(N for NO, anything else for YES)?".format(Word))
                    print("\n")
                    
                    if( Choice == "N" ):
                        print("Okay, disregarding this word")
                        
                    else:
                        LetterLinkMemory.addWord(Word)
                        print("\nThank you, your word \"{0}\" has been processed.\n".format(Word))
                
                