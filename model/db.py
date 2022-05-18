import sqlite3
import pandas as pd
import csv


con = sqlite3.connect('model/database.db')
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



def addData(table, dataList, foreignKey = 'None'):
    """
    This function will fill the table passed in parameter from the data of a csv file.
    - the datalist indicates which columns to select in the csv file
    - the foreign key is optional
    """
    with open('model/data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        for row in reader:
            query = 'SELECT (ID) FROM ' + table + ' WHERE ' + dataList[0] + '="{}";'.format(row[dataList[0]])
            result = cur.execute(query)

            if result.fetchone() == None:
                newElement = []
                columnElement = ''
                for column in dataList:
                    newElement.append(row[column])
                    columnElement = columnElement + column
                    if column != dataList[-1]:
                        columnElement = columnElement + ','
                
                if foreignKey != 'None':
                    query = 'SELECT ID FROM ' + foreignKey[0] + ' WHERE ' + foreignKey[1] + ' = "{}"'.format(row[foreignKey[1]])
                    fkID = cur.execute(query)
                    newElement.append(fkID.fetchone()[0])
                    columnElement = columnElement + ',' + foreignKey[0] + 'ID'      
                 
                qMark = '?,' * (len(newElement)-1) + '?'
                query = 'INSERT INTO ' + table + ' (' + columnElement + ') VALUES (' + qMark + ');'
                cur.execute(query, newElement)
                


valleyList = ['Valley']
stationList = ['Station', 'Range', 'Altitude']
treeList = ['code', 'VH', 'H', 'SH']
harvestList = ['ID', 'harv_num', 'DD', 'harv', 'Year', 'Date', 'Mtot', 'Ntot', 'Ntot1', 'oneacorn', 'tot_Germ', 'M_Germ', 'N_Germ', 'rate_Germ']


addData('Valley', valleyList)
addData('Station', stationList, ('Valley', 'Valley'))
addData('Tree', treeList, ('Station', 'Station'))
addData('Harvest', harvestList, ('Tree', 'code'))


con.commit()
con.close()
