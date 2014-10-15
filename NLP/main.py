import LetterLinkMemory
import Mainmenu

LetterLinkMemory.link("LetterLinkMemory.db", 
                """
                CREATE TABLE IF NOT EXISTS preceding_letter_frequencies(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    letter varchar(5),
                    preceding_letter varchar(5),
                    preceding_preceding_letter varchar(5),
                    count int
                );
                CREATE TABLE IF NOT EXISTS succeeding_letter_frequencies(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    letter varchar(5),
                    succeeding_letter varchar(5),
                    succeeding_succeeding_letter varchar(5),
                    count int
                );
                """)

print("Welcome to rev 3 of the Learning Word Parser!")

while (True):
    
    print(
    
            """
            Please select an option to continue:
            
                (a) Add a word to the WordMemory.
                (b) Scan a string for words
                (c) Quit
            """
    
    )
    
    Choice = input()
    
    if(   Choice == 'a' ):
        Mainmenu.doAddWords()
        
    elif( Choice == 'b' ):
        Mainmenu.doScanString()
    
    elif( Choice == 'c' ):
        break
    
LetterLinkMemory.delink()