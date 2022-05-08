import sqlite3
import pandas as pd
import csv


con = sqlite3.connect('database.db')
cur = con.cursor()


cur.execute('''
    CREATE TABLE IF NOT EXISTS Valley (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL UNIQUE
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


def addData(table, dataList):
    with open('data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            if table == 'Valley' :
                query = 'SELECT (id) INTO Valley WHERE nom="{}"'.format(row['Valley'])
            elif table == 'Station' :
                query = 'SELECT (id) INTO Station WHERE nom="{}"'.format(row['Station'])
            elif table == 'Tree' :
                query = 'SELECT (id) INTO Tree WHERE nom="{}"'.format(row['Tree'])
            else :
                query = 'SELECT (id) INTO Harvest WHERE nom="{}"'.format(row['Harvest'])
            result = cur.execute(query)
            if result.fetchone() == None:
                r = row[dataList]
                r.to_sql(table, con, if_exists='append', index=False)


valleyList = ['Valley']
stationList = ['Station', 'Range', 'Altitude']
treeList = ['code', 'VH', 'H', 'SH']
harvestList = ['ID', 'harv_num', 'DD', 'harv', 'Year', 'Date', 'Mtot', 'Ntot', 'Ntot1', 'oneacorn', 'tot_Germ', 'M_Germ', 'N_Germ', 'rate_Germ']


addData('Valley', valleyList)
addData('Station', stationList)
addData('Tree', treeList)
addData('Harvest', harvestList)
