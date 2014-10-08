import sqlite3

"""
A file for connecting to and handling the databases for memory.
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
        if( i + 2 < len(Letters) ):
            db.execute('SELECT * FROM succeeding_letter_frequencies WHERE letter=? AND succeeding_letter=? AND succeeding_succeeding_letter=?', 
                       (Character, Letters[i + 1], Letters[i + 2]))
            
            if( db.fetchone() is None ):
                db.execute('INSERT INTO succeeding_letter_frequencies (letter, succeeding_letter, succeeding_succeeding_letter, count)' + 
                           'VALUES (?, ?, ?, 1)', (Character, Letters[i + 1], Letters[i + 2]))
                update()
                
            else:
                db.execute('UPDATE succeeding_letter_frequencies SET count = count + 1 WHERE letter=? AND succeeding_letter=? AND succeeding_succeeding_letter=?', 
                           (Character, Letters[i + 1], Letters[i + 2]))
                update()
                
        elif( i + 1 < len(Letters) ):
            db.execute('SELECT * FROM succeeding_letter_frequencies WHERE letter=? AND succeeding_letter=? AND succeeding_succeeding_letter=?', 
                       (Character, Letters[i + 1], ''))
            
            if( db.fetchone() is None ):
                db.execute('INSERT INTO succeeding_letter_frequencies (letter, succeeding_letter, succeeding_succeeding_letter, count)' + 
                           'VALUES (?, ?, ?, 1)', (Character, Letters[i + 1], ''))
                update()
                
            else:
                db.execute('UPDATE succeeding_letter_frequencies SET count = count + 1 WHERE letter=? AND succeeding_letter=? AND succeeding_succeeding_letter=?', 
                           (Character, Letters[i + 1], ''))
                update()
                
        else:
            db.execute('SELECT * FROM succeeding_letter_frequencies WHERE letter=? AND succeeding_letter=? AND succeeding_succeeding_letter=?', 
                       (Character, None, ''))
            
            if( db.fetchone() is None ):
                db.execute('INSERT INTO succeeding_letter_frequencies (letter, succeeding_letter, succeeding_succeeding_letter, count)' + 
                           'VALUES (?, ?, ?, 1)', (Character, None, ''))
                update()
                
            else:
                db.execute('UPDATE succeeding_letter_frequencies SET count = count + 1 WHERE letter=? AND succeeding_letter=? AND succeeding_succeeding_letter=?', 
                           (Character, None, ''))
                update()
                
    Letters = Word[::-1]
    
    for (i, Character) in enumerate(Letters):             
        if( i + 2 < len(Letters) ):
            db.execute('SELECT * FROM preceding_letter_frequencies WHERE letter=? AND preceding_letter=? AND preceding_preceding_letter=?', 
                       (Character, Letters[i + 1], Letters[i + 2]))
            
            if( db.fetchone() is None ):
                db.execute('INSERT INTO preceding_letter_frequencies (letter, preceding_letter, preceding_preceding_letter, count)' + 
                           'VALUES (?, ?, ?, 1)', (Character, Letters[i + 1], Letters[i + 2]))
                update()
                
            else:
                db.execute('UPDATE preceding_letter_frequencies SET count = count + 1 WHERE letter=? AND preceding_letter=? AND preceding_preceding_letter=?', 
                           (Character, Letters[i + 1], Letters[i + 2]))
                update()
                
        elif( i + 1 < len(Letters) ):
            db.execute('SELECT * FROM preceding_letter_frequencies WHERE letter=? AND preceding_letter=? AND preceding_preceding_letter=?', 
                       (Character, Letters[i + 1], ''))
            
            if( db.fetchone() is None ):
                db.execute('INSERT INTO preceding_letter_frequencies (letter, preceding_letter, preceding_preceding_letter, count)' + 
                           'VALUES (?, ?, ?, 1)', (Character, Letters[i + 1], ''))
                update()
                
            else:
                db.execute('UPDATE preceding_letter_frequencies SET count = count + 1 WHERE letter=? AND preceding_letter=? AND preceding_preceding_letter=?', 
                           (Character, Letters[i + 1], ''))
                update()
                
        else:
            db.execute('SELECT * FROM preceding_letter_frequencies WHERE letter=? AND preceding_letter=? AND preceding_preceding_letter=?', 
                       (Character, None, ''))
            
            if( db.fetchone() is None ):
                db.execute('INSERT INTO preceding_letter_frequencies (letter, preceding_letter, preceding_preceding_letter, count)' + 
                           'VALUES (?, ?, ?, 1)', (Character, None, ''))
                update()
                
            else:
                db.execute('UPDATE preceding_letter_frequencies SET count = count + 1 WHERE letter=? AND preceding_letter=? AND preceding_preceding_letter=?', 
                           (Character, None, ''))
                update()
            

def scanForWords( String ):
    Words = []
    
    for i in range(0, len(String) - 1 ):
        db.execute('SELECT * FROM succeeding_letter_frequencies WHERE letter=? AND succeeding_letter=? AND succeeding_succeeding_letter=?', 
                   (String[i], String[i + 1], String[i + 2]))
        
        Word = ""
        
        if( db.fetchone() is None ):
            continue
        
        else:
            FetechedOne = True
            
            while( i < len(String) - 2 and FetechedOne is True ):
                print("We are intepreting {0}{1}{2} of the string\n".format(String[i], String[i - 1], String[i - 2]))
                Word += String[i]
                i += 2
                
                db.execute('SELECT * FROM preceding_letter_frequencies WHERE letter=? AND preceding_letter=? AND preceding_preceding_letter=?', 
                           (String[i], String[i - 1], String[i - 2]))
                
                if( db.fetchone() is not None ):
                    FetchedOne = True
                    
                else:
                    break
            
            Words.append(Word)
    
    return Words
        
    
def update():
    global dbConnection, db
    
    dbConnection.commit()
    
def delink():
    global dbConnection, db
    
    dbConnection.close()
    
