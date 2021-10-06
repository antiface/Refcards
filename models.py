import sqlite3 as sql
import os

os.chdir('FILEPATH')

def create_card(context, refcard):
    con = sql.connect('database.db')
    cur = con.cursor()
    cur.execute('insert into refcards (context, refcard) values(?, ?)', (context, refcard))
    con.commit()
    con.close()

def get_cards():
    con = sql.connect('database.db')
    cur = con.cursor()
    cur.execute('select * from refcards')
    refcards = cur.fetchall()
    return refcards
