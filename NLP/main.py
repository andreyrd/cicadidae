import WordMemory
import Mainmenu

WordMemory.link("words.db", 
                """
                CREATE TABLE IF NOT EXISTS preceding_letter_frequencies(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    letter varchar(1),
                    preceding_letter varchar(1),
                    preceding_preceding_letter varchar(1),
                    count int
                );
                CREATE TABLE IF NOT EXISTS succeeding_letter_frequencies(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    letter varchar(1),
                    succeeding_letter varchar(1),
                    succeeding_succeeding_letter varchar(1),
                    count int
                );
                """)

print("Welcome to rev 2 of the Learning Word Parser!")

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
    
WordMemory.delink()