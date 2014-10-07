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
        if( i + 1 < len(Letters) ):
            db.execute('SELECT * FROM succeeding_letter_frequencies WHERE letter=? AND succeeding_letter=?', (Character, Letters[i + 1]))
            
            if( db.fetchone() is None ):
                db.execute('INSERT INTO succeeding_letter_frequencies (letter, succeeding_letter, count)' + 
                           'VALUES (?, ?, 1)', (Character, Letters[i + 1]))
                update()
                
            else:
                db.execute('UPDATE succeeding_letter_frequencies SET count = count + 1 WHERE letter=? AND succeeding_letter=?', (Character, Letters[i + 1]))
                update()
            
        else:
            db.execute('SELECT * FROM succeeding_letter_frequencies WHERE letter=? AND succeeding_letter=?', (Character, ''))
            
            if( db.fetchone() is None ):   
                db.execute('INSERT INTO succeeding_letter_frequencies (letter, succeeding_letter, count)' + 
                           'VALUES (?, ?, 1)', (Character, ''))
                update()
                
            else:
                db.execute('UPDATE succeeding_letter_frequencies SET count = count + 1 WHERE letter=? AND succeeding_letter=?', (Character, ''))
                update()
                
    Letters = Word[::-1]
    
    for (i, Character) in enumerate(Letters):             
        if( i + 1 < len(Letters) ):
            db.execute('SELECT * FROM preceding_letter_frequencies WHERE letter=? AND preceding_letter=?', (Character, Letters[i + 1]))
                        
            if( db.fetchone() is None):
                db.execute('INSERT INTO preceding_letter_frequencies (letter, preceding_letter, count)' + 
                           'VALUES (?, ?, 1)', (Character, Letters[i + 1]))
                update()
                
            else:
                db.execute('UPDATE preceding_letter_frequencies SET count = count + 1 WHERE letter=? AND preceding_letter=?', (Character, Letters[i + 1]))
                update()
            
        else:
            db.execute('SELECT * FROM preceding_letter_frequencies WHERE letter=? AND preceding_letter=?', (Character, ''))
            
            if( db.fetchone() is None ):   
                db.execute('INSERT INTO preceding_letter_frequencies (letter, preceding_letter, count)' + 
                           'VALUES (?, ?, 1)', (Character, ''))
                update()
                
            else:
                db.execute('UPDATE preceding_letter_frequencies SET count = count + 1 WHERE letter=? AND preceding_letter=?', (Character, ''))
                update()
            

    
def update():
    global dbConnection, db
    
    dbConnection.commit()
    
def delink():
    global dbConnection, db
    
    dbConnection.close()
    
