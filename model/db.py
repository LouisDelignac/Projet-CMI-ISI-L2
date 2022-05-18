import sqlite3
import pandas as pd
import csv


con = sqlite3.connect('database.db')
cur = con.cursor()


cur.execute('''
    CREATE TABLE IF NOT EXISTS Valley (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Valley TEXT NOT NULL
    );
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Station (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Station TEXT,
    Range INTEGER,
    Altitude INTEGER,
    ValleyID INT,
    FOREIGN KEY (ValleyID) REFERENCES Valley(ID)
    );
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Tree (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL,
    VH REAL,
    H REAL,
    SH REAL,
    StationID INT NOT NULL,
    FOREIGN KEY (StationID) REFERENCES Station(ID)
    );
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Harvest (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    HarvestID TEXT NOT NULL,
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
    TreeID INTEGER NOT NULL,
    FOREIGN KEY (TreeID) REFERENCES Tree(ID)
    );
''')


def addData(table, dataList):
    with open('data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            query = 'SELECT (ID) FROM ' + table + ' WHERE ' + dataList[0] + '="{}";'.format(row[table])
            result = cur.execute(query)
            if result.fetchone() == None:
                for column in dataList:
                    query = 'INSERT INTO ' + table + ' (' + column + ') VALUES (?);'
                    cur.execute(query, (row[column], ))
                if table == 'Station':
                    query = 'SELECT ID FROM Valley WHERE Valley = "{}"'.format(row['Valley'])
                    test = cur.execute(query)
                    test2 = test.fetchone()
                    query = 'INSERT INTO Station (ValleyID) VALUES ({});'.format(test2[0])
                    cur.execute(query)


valleyList = ['Valley']
stationList = ['Station', 'Range', 'Altitude']
treeList = ['code', 'VH', 'H', 'SH']
harvestList = ['ID', 'harv_num', 'DD', 'harv', 'Year', 'Date', 'Mtot', 'Ntot', 'Ntot1', 'oneacorn', 'tot_Germ', 'M_Germ', 'N_Germ', 'rate_Germ']


addData('Valley', valleyList)
addData('Station', stationList)
#addData('Tree', treeList)
#addData('Harvest', harvestList)


con.commit()
con.close()