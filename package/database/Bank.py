import sqlite3
connection = sqlite3.connect('infos.db')
cursor = connection.cursor()

class BankInfo:
    def __init__(self):
        global connection
        global cursor
        connection = sqlite3.connect('infos.db')
        cursor = connection.cursor()

    def insert(self, name, description,):
        cursor.execute('INSERT INTO info VALUES(?,?)', (name, description))
        connection.commit()

    def update(self, name, description):
        cursor.execute('UPDATE info SET description = ? WHERE name = ? ', (description, name))
        connection.commit()

    def delete(self, name):
        cursor.execute("DELETE FROM info WHERE name = ?", (name,))
        connection.commit()

    def getNames(self):
        sql = 'SELECT * FROM info '
        listNames = []
        for row in cursor.execute(sql):
            listNames.insert(0, row[0])
        return listNames

    def getDescription(self, name):
        sql = 'SELECT * FROM info WHERE name = ?'
        for row in cursor.execute(sql, (name,)):
            description = row[1]
        return description

    def close(self):
        cursor.close()
        connection.close()