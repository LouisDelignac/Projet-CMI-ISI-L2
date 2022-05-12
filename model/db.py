import sqlite3
import pandas as pd
import csv


con = sqlite3.connect('database.db')
cur = con.cursor()


cur.execute('''
    CREATE TABLE IF NOT EXISTS Valley (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Valley TEXT NOT NULL UNIQUE
    );
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Station (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL UNIQUE,
    ValleyID INT NOT NULL,
    Range INTEGER,
    Altitude INTEGER,
    FOREIGN KEY (ValleyID) REFERENCES Valley(ID)
    );
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Tree (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    StationID INT NOT NULL,
    VH REAL,
    H REAL,
    SH REAL,
    FOREIGN KEY (StationID) REFERENCES Station(ID)
    );
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Harvest (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    HarvestID TEXT NOT NULL,
    TreeID INTEGER NOT NULL,
    harv_num REAL,
    DD REAL,
    harv REAL,
    Year INTEGER,
    Date DATETIME,
    Mtot REAL,
    Ntot REAL,
    Ntot1 REAL,
    oneacorn REAL,
    tot_Germ REAL,
    M_Germ REAL,
    N_Germ REAL,
    rate_Germ REAL,
    FOREIGN KEY (TreeID) REFERENCES Tree(ID)
    );
''')


data = pd.read_csv('data.csv', sep=';') 
data.to_sql('ReproData', con, if_exists='replace', index=False)


def addData(table, dataList):
    if table == 'Valley':
        query = "INSERT OR IGNORE INTO Valley (Valley) SELECT DISTINCT 'Valley' FROM ReproData"
        cur.execute(query)


valleyList = ['Valley']
stationList = ['Station', 'Range', 'Altitude']
treeList = ['code', 'VH', 'H', 'SH']
harvestList = ['ID', 'harv_num', 'DD', 'harv', 'Year', 'Date', 'Mtot', 'Ntot', 'Ntot1', 'oneacorn', 'tot_Germ', 'M_Germ', 'N_Germ', 'rate_Germ']


addData('Valley', valleyList)
#addData('Station', stationList)
#addData('Tree', treeList)
#addData('Harvest', harvestList)
