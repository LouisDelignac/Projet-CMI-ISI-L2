import sqlite3
import pandas as pd


con = sqlite3.connect('database.db')
cur = con.cursor()


cur.execute('''
    CREATE TABLE IF NOT EXISTS Valley (
    ID INT PRIMARY KEY AUTOINCREMENT,
    Valley TEXT NOT NULL UNIQUE
    );
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Station (
    ID INT PRIMARY KEY AUTOINCREMENT,
    Station TEXT NOT NULL UNIQUE,
    ValleyID INT NOT NULL,
    Range INT,
    Altitude INT,
    FOREIGN KEY (ValleyID) REFERENCES Valley(ID)
    );
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Arbre (
    ID INT PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    StationID INT NOT NULL,
    VH REAL,
    H REAL,
    SH REAL,
    FOREIGN KEY (StationID) REFERENCES Station(ID)
    );
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Recolte (
    ID INT PRIMARY KEY AUTOINCREMENT,
    harvestID TEXT NOT NULL,
    ArbreID INT NOT NULL,
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
    FOREIGN KEY (ArbreID) REFERENCES Arbre(ID)
    );
''')


data = pd.read_csv('data.csv', sep=';') 
data.to_sql('ReproData', con, if_exists='replace', index=False)


def addData(dataList):
    r = data[dataList]
    r.to_sql('Recolte', con, if_exists='append', index=False)


valleyList = ['Valley']
stationList = ['Station', 'Range', 'Altitude']
treeList = ['code', 'VH', 'H', 'SH']
harvestList = ['ID', 'harv_num', 'DD', 'harv', 'Year', 'Date', 'Mtot', 'Ntot', 'Ntot1', 'oneacorn', 'tot_Germ', 'M_Germ', 'N_Germ', 'rate_Germ']


addData(valleyList)
addData(stationList)
addData(treeList)
addData(harvestList)
