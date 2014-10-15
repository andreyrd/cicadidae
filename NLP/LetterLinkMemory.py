import sqlite3

"""
A file for connecting to and handling the databases for LetterLinkMemory.
it encapsulates sqlite3's functionality too.
"""

dbConnection = None
db = None

    
def link( Filename, InitialDatabaseStructure = False ):
    
    global dbConnection, db
    
    DatabaseFilename = Filename
    dbConnection = sqlite3.connect(Filename)
    db = dbConnection.cursor()
    
    if( InitialDatabaseStructure is not False ):

        db.executescript(InitialDatabaseStructure)
        update()
    
def addWord( Word ):
    
    global dbConnection, db
    
    Letters = list(Word)
    
    for (i, Character) in enumerate(Letters):           
        if( i + 2 < len(Letters)):
            db.execute('SELECT * FROM succeeding_letter_frequencies WHERE letter=? AND succeeding_letter=? AND succeeding_succeeding_letter=?', 
                       (Character, Letters[i + 1], Letters[i + 2]))
            
            if not db.fetchone():
                db.execute('INSERT INTO succeeding_letter_frequencies (letter, succeeding_letter, succeeding_succeeding_letter, count)' + 
                           'VALUES (?, ?, ?, 1)', (Character, Letters[i + 1], Letters[i + 2]))
                update()
                
            else:
                db.execute('UPDATE succeeding_letter_frequencies SET count = count + 1 WHERE letter=? AND succeeding_letter=? AND succeeding_succeeding_letter=?', 
                           (Character, Letters[i + 1], Letters[i + 2]))
                update()
                
        elif( i + 1 < len(Letters)):
            db.execute('SELECT * FROM succeeding_letter_frequencies WHERE letter=? AND succeeding_letter=? AND succeeding_succeeding_letter=?', 
                       (Character, Letters[i + 1], "EMPTY"))
            
            if not db.fetchone():
                db.execute('INSERT INTO succeeding_letter_frequencies (letter, succeeding_letter, succeeding_succeeding_letter, count)' + 
                           'VALUES (?, ?, ?, 1)', (Character, Letters[i + 1], "EMPTY"))
                update()
                
            else:
                db.execute('UPDATE succeeding_letter_frequencies SET count = count + 1 WHERE letter=? AND succeeding_letter=? AND succeeding_succeeding_letter=?', 
                           (Character, Letters[i + 1], "EMPTY"))
                update()
                
        else:
            db.execute('SELECT * FROM succeeding_letter_frequencies WHERE letter=? AND succeeding_letter=? AND succeeding_succeeding_letter=?', 
                       (Character, "EMPTY", "EMPTY"))
            
            if not db.fetchone():
                db.execute('INSERT INTO succeeding_letter_frequencies (letter, succeeding_letter, succeeding_succeeding_letter, count)' + 
                           'VALUES (?, ?, ?, 1)', (Character, "EMPTY", "EMPTY"))
                update()
                
            else:
                db.execute('UPDATE succeeding_letter_frequencies SET count = count + 1 WHERE letter=? AND succeeding_letter=? AND succeeding_succeeding_letter=?', 
                           (Character, "EMPTY", "EMPTY"))
                update()
                
    Letters = Word[::-1]
    
    for (i, Character) in enumerate(Letters):             
        if( i + 2 < len(Letters)):
            db.execute('SELECT * FROM preceding_letter_frequencies WHERE letter=? AND preceding_letter=? AND preceding_preceding_letter=?', 
                       (Character, Letters[i + 1], Letters[i + 2]))
            
            if not db.fetchone():
                db.execute('INSERT INTO preceding_letter_frequencies (letter, preceding_letter, preceding_preceding_letter, count)' + 
                           'VALUES (?, ?, ?, 1)', (Character, Letters[i + 1], Letters[i + 2]))
                update()
                
            else:
                db.execute('UPDATE preceding_letter_frequencies SET count = count + 1 WHERE letter=? AND preceding_letter=? AND preceding_preceding_letter=?', 
                           (Character, Letters[i + 1], Letters[i + 2]))
                update()
                
        elif( i + 1 < len(Letters)):
            db.execute('SELECT * FROM preceding_letter_frequencies WHERE letter=? AND preceding_letter=? AND preceding_preceding_letter=?', 
                       (Character, Letters[i + 1], "EMPTY"))
            
            if not db.fetchone():
                db.execute('INSERT INTO preceding_letter_frequencies (letter, preceding_letter, preceding_preceding_letter, count)' + 
                           'VALUES (?, ?, ?, 1)', (Character, Letters[i + 1], "EMPTY"))
                update()
                
            else:
                db.execute('UPDATE preceding_letter_frequencies SET count = count + 1 WHERE letter=? AND preceding_letter=? AND preceding_preceding_letter=?', 
                           (Character, Letters[i + 1], "EMPTY"))
                update()
                
        else:
            db.execute('SELECT * FROM preceding_letter_frequencies WHERE letter=? AND preceding_letter=? AND preceding_preceding_letter=?', 
                       (Character, "EMPTY", "EMPTY"))
            
            if not db.fetchone():
                db.execute('INSERT INTO preceding_letter_frequencies (letter, preceding_letter, preceding_preceding_letter, count)' + 
                           'VALUES (?, ?, ?, 1)', (Character, "EMPTY", "EMPTY"))
                update()
                
            else:
                db.execute('UPDATE preceding_letter_frequencies SET count = count + 1 WHERE letter=? AND preceding_letter=? AND preceding_preceding_letter=?', 
                           (Character, "EMPTY", "EMPTY"))
                update()
            

def scanForWords( String ):
    global dbConnection, db
    
    if String != "": #If the string is not empty
        Words = String.split()
        
        DetectedWords = []
        
        for UnknownWord in Words:
            Word = ""
            
            i = 0
            while i < len(UnknownWord):
                if(   (len(UnknownWord) - 1) - i == 1 ):
                    db.execute('SELECT * FROM succeeding_letter_frequencies WHERE letter=? AND succeeding_letter=? AND succeeding_succeeding_letter=?', 
                            (UnknownWord[i], UnknownWord[i + 1], "EMPTY"))
                    
                    if not db.fetchone():
                        break
                    
                    else:
                        Word = Word + UnknownWord[i] + UnknownWord[i + 1]
                        break
                    
                elif( (len(UnknownWord) - 1) - i == 0 ):
                    db.execute('SELECT * FROM succeeding_letter_frequencies WHERE letter=? AND succeeding_letter=? AND succeeding_succeeding_letter=?', 
                            (UnknownWord[i], "EMPTY", "EMPTY"))
                    
                    if not db.fetchone():
                        break
                    
                    else:
                        Word = Word + UnknownWord[i]
                        break
                                                    
                elif( (len(UnknownWord) - 1) - i < 0 ):
                    break
                
                else:
                    db.execute('SELECT * FROM succeeding_letter_frequencies WHERE letter=? AND succeeding_letter=? AND succeeding_succeeding_letter=?', 
                            (UnknownWord[i], UnknownWord[i + 1], UnknownWord[i + 2]))
                    
                    if not db.fetchone():
                        break
                    
                    else:
                        Word = Word + UnknownWord[i] + UnknownWord[i + 1] + UnknownWord[i + 2]
                    
                i = i + 3 #increment i by three since python is stupid
                
            
            DetectedWords.append(Word)
        
        return DetectedWords
    return []

def update():
    global dbConnection, db
    
    dbConnection.commit()
    
def delink():
    global dbConnection, db
    
    dbConnection.close()
    
