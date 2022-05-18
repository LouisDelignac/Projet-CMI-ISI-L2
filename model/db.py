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
    Station TEXT NOT NULL,
    Range INTEGER,
    Altitude INTEGER,
    ValleyID INT NOT NULL,
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
    HarvestID INTEGER PRIMARY KEY AUTOINCREMENT,
    ID TEXT NOT NULL,
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
            query = 'SELECT (ID) FROM ' + table + ' WHERE ' + dataList[0] + '="{}";'.format(row[dataList[0]])
            result = cur.execute(query)
            if result.fetchone() == None:
                newElement = []
                ratio = ''
                for column in dataList:
                    newElement.append(row[column])
                    ratio = ratio + column
                    if column != dataList[-1]:
                        ratio = ratio + ','
                if table == 'Station':
                    query = 'SELECT ID FROM Valley WHERE Valley = "{}"'.format(row['Valley'])
                    test = cur.execute(query)
                    test2 = test.fetchone()
                    newElement.append(test2[0])
                    ratio = ratio + ',ValleyID'
                elif table == 'Tree':
                    query = 'SELECT ID FROM Station WHERE Station = "{}"'.format(row['Station'])
                    test = cur.execute(query)
                    test2 = test.fetchone()
                    newElement.append(test2[0])
                    ratio = ratio + ',StationID'
                elif table == 'Harvest':
                    query = 'SELECT ID FROM Tree WHERE code = "{}"'.format(row['code'])
                    test = cur.execute(query)
                    test2 = test.fetchone()
                    newElement.append(test2[0])
                    ratio = ratio + ',TreeID'
                interro = '?,' * (len(newElement)-1) + '?'
                query = 'INSERT INTO ' + table + ' (' + ratio + ') VALUES (' + interro + ');'
                cur.execute(query, newElement)
                


valleyList = ['Valley']
stationList = ['Station', 'Range', 'Altitude']
treeList = ['code', 'VH', 'H', 'SH']
harvestList = ['ID', 'harv_num', 'DD', 'harv', 'Year', 'Date', 'Mtot', 'Ntot', 'Ntot1', 'oneacorn', 'tot_Germ', 'M_Germ', 'N_Germ', 'rate_Germ']


addData('Valley', valleyList)
addData('Station', stationList)
addData('Tree', treeList)
addData('Harvest', harvestList)


con.commit()
con.close()